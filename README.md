<h1 align="center">🕒 TickTrack — Clock Time Detection using OpenCV</h1>

<p align="center">
  <em>Detect analog clock time automatically using OpenCV, geometric analysis, and intelligent line filtering.</em>
</p>

<hr>

<h2>📘 Overview</h2>

<p>
<b>TickTrack</b> is a computer vision tool that reads analog clocks from images and determines the time shown.
It identifies the hour and minute hands using <code>Hough Circle</code> and <code>Hough Line</code> transforms, filters unwanted red second hands, and estimates angles relative to the clock center.
</p>

<details>
  <summary><b>✨ Core Idea</b></summary>
  <ul>
    <li>Detect the circular clock face using <code>cv2.HoughCircles</code>.</li>
    <li>Find all candidate lines (clock hands) with <code>cv2.HoughLinesP</code>.</li>
    <li>Filter those near the detected center and remove duplicates by angle.</li>
    <li>Identify the <b>minute hand</b> as the longest line, and the <b>hour hand</b> as the shorter one.</li>
    <li>Calculate their angles to infer the actual time.</li>
  </ul>
</details>

<hr>

<h2>🚀 Installation & Setup</h2>

<pre>
git clone https://github.com/Niklaus2003/TickTrack-clock-detection.git
cd TickTrack-clock-detection
pip install opencv-python numpy
</pre>

<p>Run the project:</p>

<pre>
python detect_clock_time.py
</pre>

<p><b>Note:</b> Replace <code>images/clock1.jpg</code> with your own image if needed.</p>

<hr>

<h2>🧩 Features</h2>

<ul>
  <li>✅ Detects clock center using circle detection</li>
  <li>🧭 Estimates angle of hour and minute hands</li>
  <li>🎨 Removes red second hand automatically</li>
  <li>🧠 Calculates time based on geometry</li>
  <li>💡 Displays detected hands and time visually</li>
</ul>

<details>
  <summary><b>🛠 How It Works (Algorithm)</b></summary>
  <ol>
    <li>Preprocess image → HSV filtering → blur → threshold.</li>
    <li>Detect clock face and find center coordinates.</li>
    <li>Use probabilistic Hough transform to detect lines.</li>
    <li>Estimate each line’s length and thickness.</li>
    <li>Pick two distinct hands (minute and hour) based on geometry.</li>
    <li>Convert the detected angles to readable time.</li>
  </ol>
</details>

<hr>

<h2>🖼 Output Example</h2>

<p>
The system overlays the detected hour and minute hands with colored lines:
<ul>
  <li><span style="color:#00FF00">Green</span> → Minute hand</li>
  <li><span style="color:#FF0000">Blue</span> → Hour hand</li>
</ul>
Displays the predicted time in terminal as:
</p>

<pre>🕒 Detected Time: 10:45</pre>

<hr>

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>📷 Real-time clock reading using webcam feed</li>
  <li>🪞 Add perspective correction for tilted images</li>
  <li>🎯 Improve noise handling using RANSAC line fitting</li>
  <li>🧾 Configurable parameters via YAML</li>
  <li>🌐 Build a small Streamlit web interface for live demos</li>
</ul>

<hr>

<h2>📦 Dependencies</h2>

<pre>
opencv-python
numpy
</pre>

<hr>

<h2>📚 Repository</h2>

<p>
🔗 <a href="https://github.com/Niklaus2003/AI_streamlit_tutorbot.git" target="_blank">GitHub Repository</a>  
(contains the <code>detect_clock_time.py</code> source with all logic for angle and thickness-based detection)
</p>

<hr>

<h2>🤝 Contributing</h2>

<p>
Feel free to fork the repository, open pull requests, or suggest improvements.
Every contribution helps enhance the algorithm’s robustness!
</p>

<hr>

<h2>📜 License</h2>

<p>
This project is open-sourced under the <b>MIT License</b>.
</p>

<hr>

<h3 align="center">⭐ If you like this project, consider starring the repo!</h3>
