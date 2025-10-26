<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>TickTrack — Clock Time Detection (README)</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#94a3b8; --accent:#22c55e; --accent2:#60a5fa;
      --mono: 'SFMono-Regular', Menlo, Monaco, "Roboto Mono", monospace;
      color-scheme: dark;
    }
    body{font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; background:linear-gradient(180deg,#071023 0%, #071826 100%); color:#e6eef8; margin:0; padding:32px;}
    .container{max-width:980px;margin:0 auto;}
    header{display:flex;gap:16px;align-items:center;margin-bottom:20px;}
    .logo{width:64px;height:64px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-weight:700;color:#001;}
    h1{margin:0;font-size:1.6rem}
    p.lead{color:var(--muted);margin:6px 0 20px}
    .card{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); padding:18px;border-radius:12px;box-shadow:0 6px 18px rgba(2,6,23,0.6);margin-bottom:16px}
    .grid{display:grid;grid-template-columns:1fr 320px;gap:16px}
    .features ul{list-style: none;padding:0;margin:0}
    .features li{padding:8px 0;border-bottom:1px dashed rgba(255,255,255,0.03);color:var(--muted)}
    pre.cmd{background:#021225;padding:12px;border-radius:8px;color:#cfeefc;font-family:var(--mono);overflow:auto}
    .btn{display:inline-block;background:var(--accent);color:#001;padding:8px 12px;border-radius:8px;font-weight:600;text-decoration:none;cursor:pointer}
    .muted{color:var(--muted)}
    details{background:rgba(255,255,255,0.01);padding:12px;border-radius:8px;margin-bottom:10px}
    summary{font-weight:600;cursor:pointer}
    footer{color:var(--muted);margin-top:18px;font-size:0.9rem}
    .img-preview{width:100%;height:240px;display:flex;align-items:center;justify-content:center;border-radius:8px;background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.005));color:var(--muted);overflow:hidden}
    .meta{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px}
    .chip{background:rgba(255,255,255,0.02);padding:6px 8px;border-radius:999px;font-size:0.85rem;color:var(--muted)}
    code.inline{background:rgba(255,255,255,0.02);padding:2px 6px;border-radius:6px;font-family:var(--mono);color:#a8f0ff}
    .copy{float:right;background:transparent;border:0;color:var(--muted);cursor:pointer}
    .note{background:linear-gradient(90deg, rgba(96,165,250,0.06), rgba(34,197,94,0.03));padding:8px;border-radius:8px;color:var(--muted);margin:8px 0}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">TT</div>
      <div>
        <h1>TickTrack — AI Clock Time Detection</h1>
        <p class="lead">Detects hour and minute hands from analog clock images using OpenCV, Hough transforms and geometric analysis — outputs visual overlay and detected time.</p>
      </div>
    </header>

    <div class="grid">
      <div>
        <div class="card features">
          <h3>Features</h3>
          <ul>
            <li>🔎 Detects clock face (Hough Circle Transform)</li>
            <li>✂️ Filters out red second hand for cleaner detection</li>
            <li>📐 Identifies hour & minute hands using Hough Line Transform and geometric heuristics</li>
            <li>⏱ Calculates time from angles and displays overlay</li>
            <li>⚙ Robust preprocessing: blur, adaptive thresholding & thickness estimation</li>
            <li>🧪 Useful for image processing demos, robotics vision, and CV learning</li>
          </ul>
        </div>

        <div class="card">
          <h3>Quick Install & Run</h3>
          <p class="muted">Create a Python environment and install dependencies:</p>
          <pre class="cmd" id="install-cmd">python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)
pip install opencv-python numpy</pre>
          <p class="muted">Run the demo:</p>
          <pre class="cmd" id="run-cmd">python detect_clock_time.py --image images/clock1.jpg</pre>
          <p class="note"><strong>Note:</strong> The repo includes a sample image at <code class="inline">images/clock1.jpg</code>. Adjust Hough parameters for different image resolutions.</p>
        </div>

        <div class="card">
          <h3>How it works (short)</h3>
          <ol>
            <li>Preprocess image: resize → HSV filter → grayscale → blur → binary threshold.</li>
            <li>Detect circular clock face using Hough Circle Transform to get center (cx, cy).</li>
            <li>Detect candidate lines (HoughLinesP); select those near the center.</li>
            <li>Estimate line thickness and length; pick longest as minute hand and next as hour hand (with duplicate-angle filtering).</li>
            <li>Compute angles relative to 12 o'clock and convert to time (hours : minutes).</li>
          </ol>
        </div>

        <div class="card">
          <h3>Usage Tips</h3>
          <ul>
            <li class="muted">If your clock is small, increase image scale or decrease <code class="inline">minRadius</code> in Hough detection.</li>
            <li class="muted">For noisy images, increase Gaussian blur kernel or tune Canny thresholds.</li>
            <li class="muted">If second hand colors vary, adjust HSV red ranges or remove by color clustering.</li>
          </ul>
        </div>

        <div class="card">
          <h3>Future Enhancements</h3>
          <ul>
            <li>📈 Improve robustness for different lighting & perspective using edge/refinement strategies</li>
            <li>🔁 Add perspective correction (detect ellipse → unwarp) for tilted clocks</li>
            <li>🎯 Use RANSAC to improve hand line fitting and reject spurious lines</li>
            <li>📸 Support live webcam mode to read clocks in real-time</li>
            <li>🧪 Add unit tests / CI and tunable parameter config file</li>
          </ul>
        </div>
      </div>

      <aside>
        <div class="card">
          <h3>Try a sample image</h3>
          <div class="img-preview" id="preview">No image selected — preview only works locally</div>
          <div style="margin-top:10px">
            <input id="file" type="file" accept="image/*" style="width:100%"/>
            <small class="muted">Select an image to preview (client-only). Processing requires the Python script.</small>
          </div>
        </div>

        <div class="card">
          <h3>Repo & License</h3>
          <p class="muted">Source: <a href="#" id="repo-link" style="color:var(--accent2);text-decoration:none">your-github-repo</a></p>
          <div class="meta">
            <span class="chip">Python</span>
            <span class="chip">OpenCV</span>
            <span class="chip">Computer Vision</span>
            <span class="chip">MIT License</span>
          </div>
        </div>

        <div class="card">
          <h3>Copy Commands</h3>
          <button class="btn" onclick="copyText('#install-cmd')">Copy Install</button>
          <button class="btn" style="background:var(--accent2)" onclick="copyText('#run-cmd')">Copy Run</button>
        </div>

        <div class="card">
          <h3>Contact</h3>
          <p class="muted">Questions, contributions and improvements welcome — open a PR or issue on GitHub.</p>
        </div>
      </aside>
    </div>

    <footer>
      <p class="muted">Made with ❤️ — TickTrack: Open-source analog clock reader. Adjust Hough and thickness thresholds for best results with specific image sets.</p>
    </footer>
  </div>

  <script>
    document.getElementById('repo-link').href = "https://github.com/Niklaus2003/AI_streamlit_tutorbot.git".replace("AI_streamlit_tutorbot", "TickTrack-clock-read"); // edit if needed

    // Preview selected image (client-side only)
    const fileInput = document.getElementById('file');
    const preview = document.getElementById('preview');
    fileInput.addEventListener('change', (ev) => {
      const file = ev.target.files[0];
      if(!file) { preview.textContent = "No image selected — preview only works locally"; return; }
      const reader = new FileReader();
      reader.onload = function(e) {
        preview.innerHTML = '<img src="'+e.target.result+'" style="max-width:100%; max-height:100%; display:block; border-radius:6px"/>';
      }
      reader.readAsDataURL(file);
    });

    // Copy helper
    function copyText(selector){
      const el = document.querySelector(selector);
      if(!el) return;
      const text = el.textContent;
      navigator.clipboard.writeText(text).then(() => {
        alert("Copied to clipboard!");
      }).catch(()=> alert("Copy failed — select and copy manually."));
    }
  </script>
</body>
</html>
