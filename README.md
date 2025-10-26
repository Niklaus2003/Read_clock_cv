# 🕒 Read_clock_cv — Analog Clock Time Detection (OpenCV + Python)

A Python project that detects analog clock hands (hour and minute) from images using OpenCV — edge detection, Hough transforms, and geometric analysis to determine and display clock time visually and numerically.

---

## Overview

Read_clock_cv reads a single image of an analog clock, detects the clock face and candidate hand lines, filters and classifies the hour and minute hands, then estimates the time shown on the clock.

This repository currently contains:
- `read_clock.py` — main script that performs detection and prints/displays the detected time and visual output.
- `images/` — directory for example input images (replace with your own images as needed).

---

## Installation

Create a virtual environment (recommended) and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
pip install --upgrade pip
pip install opencv-python numpy
```

If the project uses any additional packages (e.g., matplotlib or imutils), install them as needed:
```bash
pip install matplotlib imutils
```

---

## Usage

Run the main script and pass an image path:

```bash
python read_clock.py <path-to-clock-image>
```

Example:

```bash
python read_clock.py images/clock1.jpg
```

The script will attempt to detect the clock center and hands, output the inferred time to the terminal, and display the annotated image with detected hands overlaid.

---

## Features

- Detects circular clock face and computes center (Hough Circle detection).
- Extracts candidate straight lines (probabilistic Hough Lines) representing clock hands.
- Filters lines near the clock center and removes duplicates by angle.
- Classifies minute and hour hands based on geometric properties (length/angle).
- Outputs detected time numerically and overlays detected hands on the image for visual verification.

---

## Example Output

The script overlays detected hands on the input image and prints a detected time, for example:

```
🕒 Detected Time: 10:45
```

Colors used in visualization may vary depending on the script's drawing logic.

---

## Contributing

Contributions, bug reports, and improvements are welcome. Please open issues or pull requests if you have enhancements or fixes.

---

## License

This project is open-sourced under the MIT License. If you would like the repository to include a LICENSE file, consider adding one with the MIT text.

---
