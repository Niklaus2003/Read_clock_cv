import cv2
import numpy as np
import math

def angle_from_center(x1, y1, x2, y2, cx, cy):
    # Choose the endpoint farther from center
    dist1 = np.hypot(x1 - cx, y1 - cy)
    dist2 = np.hypot(x2 - cx, y2 - cy)
    if dist2 > dist1:
        end_x, end_y = x2, y2
    else:
        end_x, end_y = x1, y1

    dx = end_x - cx
    dy = end_y - cy

    # Compute angle (0° is at 12 o'clock, clockwise positive)
    angle_rad = math.atan2(dy, dx)
    angle_deg = (math.degrees(angle_rad) + 360 + 90) % 360  # +90 shifts 3→0 o'clock
    return angle_deg

def is_near_center(x, y, cx, cy, threshold=40):
    return np.hypot(x - cx, y - cy) < threshold

def estimate_line_thickness(binary_img, coords):
    x1, y1, x2, y2 = coords
    mask = np.zeros_like(binary_img)
    cv2.line(mask, (x1, y1), (x2, y2), 255, 3)
    overlap = cv2.bitwise_and(binary_img, mask)
    return cv2.countNonZero(overlap) / (np.hypot(x2 - x1, y2 - y1) + 1e-6)

def remove_near_duplicate_angles(candidates, angle_thresh=10):
    filtered = []
    for cand in candidates:
        _, angle, _, _ = cand
        if all(min(abs(angle - a[1]), 360 - abs(angle - a[1])) > angle_thresh for a in filtered):
            filtered.append(cand)
    return filtered

def detect_clock_time(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("❌ Image not found.")
        return

    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Remove red second hand
    red1 = cv2.inRange(hsv, (0, 70, 50), (10, 255, 255))
    red2 = cv2.inRange(hsv, (170, 70, 50), (180, 255, 255))
    red_mask = cv2.bitwise_or(red1, red2)
    img[red_mask > 0] = (255, 255, 255)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    bin_img = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Detect clock circle
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, gray.shape[0] / 4,
                               param1=100, param2=80, minRadius=100, maxRadius=500)
    if circles is None:
        print("❌ No clock face detected.")
        return
    cx, cy, _ = np.uint16(np.around(circles[0][0]))
    cv2.circle(img, (cx, cy), 3, (0, 0, 255), -1)

    # Detect lines
    edges = cv2.Canny(blur, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 97, minLineLength=50, maxLineGap=10)
    if lines is None:
        print("❌ No lines found.")
        return

    hand_candidates = []
    for x1, y1, x2, y2 in lines[:, 0]:
        if is_near_center(x1, y1, cx, cy) or is_near_center(x2, y2, cx, cy):
            angle = angle_from_center(x1, y1, x2, y2, cx, cy)
            length = np.hypot(x2 - x1, y2 - y1)
            thickness = estimate_line_thickness(bin_img, (x1, y1, x2, y2))
            if thickness > 1.0:
                hand_candidates.append((length, angle, thickness, (x1, y1, x2, y2)))

    if not hand_candidates:
        print("❌ No valid hands found.")
        return

    # 🔁 Sort by length (longest = minute hand, shorter = hour hand)
    hand_candidates.sort(key=lambda x: -x[0])
    unique_candidates = remove_near_duplicate_angles(hand_candidates)

    if len(unique_candidates) < 2:
        print("❌ Not enough distinct hands.")
        return

    minute_line = unique_candidates[0]
    hour_line = unique_candidates[1]

    # Draw
    for label, (_, angle, thick, (x1, y1, x2, y2)) in zip(["Minute", "Hour"], [minute_line, hour_line]):
        color = (0, 255, 0) if label == "Minute" else (255, 0, 0)
        cv2.line(img, (x1, y1), (x2, y2), color, 3)
        print(f"{label} ➜ Angle = {angle:.2f}°, Length = {np.hypot(x2 - x1, y2 - y1):.2f}")

    # Time calculation
    minute_angle = minute_line[1]
    hour_angle = hour_line[1]
    minute = int(round(minute_angle / 6)) % 60
    hour = int(hour_angle // 30) % 12
    hour = 12 if hour == 0 else hour

    print(f"\n🕒 Detected Time: {hour:02d}:{minute:02d}")

    cv2.imshow("Clock Time Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run it
detect_clock_time("images\clock1.jpg")
