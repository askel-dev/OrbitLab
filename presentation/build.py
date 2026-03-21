"""Build the presentation HTML with embedded base64 images."""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(SCRIPT_DIR, "images.json"), "r") as f:
    imgs = json.load(f)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OrbitLab - Gymnasiearbete</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/black.css">
<style>
  :root {{
    --r-background-color: #0a0f1e;
    --r-main-font: "Segoe UI", system-ui, sans-serif;
    --r-heading-font: "Segoe UI", system-ui, sans-serif;
    --r-main-color: #e0e6f0;
    --r-heading-color: #ffffff;
    --r-link-color: #4ec9b0;
  }}
  .reveal {{ font-size: 28px; }}
  .reveal h1 {{ font-size: 2.2em; font-weight: 700; }}
  .reveal h2 {{ font-size: 1.6em; font-weight: 600; color: #4ec9b0; }}
  .reveal h3 {{ font-size: 1.2em; font-weight: 600; color: #6dd5c0; }}
  .reveal .subtitle {{ color: #a0aac0; font-size: 0.9em; margin-top: 0.3em; }}
  .reveal .author {{ color: #8090b0; font-size: 0.8em; margin-top: 1.5em; }}
  .reveal img {{ max-height: 55vh; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,0,0,0.5); }}
  .reveal .two-col {{ display: flex; gap: 2em; align-items: flex-start; }}
  .reveal .two-col > div {{ flex: 1; }}
  .reveal .two-col img {{ max-height: 45vh; }}
  .reveal .formula {{
    background: rgba(78, 201, 176, 0.1);
    border-left: 3px solid #4ec9b0;
    padding: 0.5em 1em;
    border-radius: 4px;
    font-family: "Consolas", monospace;
    font-size: 0.95em;
    margin: 0.5em 0;
  }}
  .reveal .highlight {{ color: #4ec9b0; font-weight: 600; }}
  .reveal .warn {{ color: #ffb444; }}
  .reveal ul {{ text-align: left; }}
  .reveal li {{ margin-bottom: 0.4em; }}
  .reveal .small {{ font-size: 0.75em; color: #8090b0; }}
  .reveal .comparison-label {{
    font-size: 0.85em;
    text-align: center;
    margin-top: 0.3em;
    color: #a0aac0;
  }}
  .slide-number {{ font-size: 14px !important; }}
  .reveal .tip-card {{
    background: rgba(78, 201, 176, 0.08);
    border: 1px solid rgba(78, 201, 176, 0.3);
    border-radius: 12px;
    padding: 0.8em 1.2em;
    margin: 0.4em 0;
    text-align: left;
  }}
  .reveal .challenge-card {{
    background: rgba(255, 180, 68, 0.08);
    border: 1px solid rgba(255, 180, 68, 0.3);
    border-radius: 12px;
    padding: 0.8em 1.2em;
    margin: 0.4em 0;
    text-align: left;
  }}
  .reveal .analogy-box {{
    background: rgba(100, 180, 255, 0.08);
    border: 1px solid rgba(100, 180, 255, 0.3);
    border-radius: 12px;
    padding: 0.8em 1.2em;
    margin: 0.6em 0;
    text-align: left;
    font-style: italic;
  }}
</style>
</head>
<body>
<div class="reveal">
<div class="slides">

<!-- ============================================================ -->
<!-- ACT 1: HOOK & CONTEXT                                        -->
<!-- ============================================================ -->

<!-- SLIDE 1: Title -->
<section>
  <h1>How Are Orbits Affected by Initial Conditions?</h1>
  <p class="subtitle">An interactive simulation of gravitation and numerical methods</p>
  <p class="author">Axel J&ouml;nsson &middot; Supervisor: Fredrik Persson</p>
  <p class="small" style="margin-top:2em;">Gymnasiearbete &mdash; Naturvetenskapsprogrammet</p>
  <aside class="notes">Welcome everyone. Today I will present my thesis project about orbital mechanics and simulation.</aside>
</section>

<!-- SLIDE 2: Real-World Hook -->
<section>
  <h2>You Used Orbital Mechanics Today</h2>
  <p style="font-size:1.2em;">Every time you open Google Maps, stream a video, or check the weather...</p>
  <div class="fragment">
    <p style="font-size:1.3em;"><span class="highlight">31 GPS satellites</span> are orbiting Earth at exactly the right speed.</p>
  </div>
  <div class="fragment">
    <p>Too slow &rarr; they crash. Too fast &rarr; they fly away.</p>
    <p style="margin-top:0.5em;">How do we figure out the <span class="highlight">exact right speed</span>?</p>
  </div>
  <aside class="notes">This is not abstract physics. This is the engineering behind technology you use every single day. The question of what speed a satellite needs is literally a life-or-death calculation for space agencies.</aside>
</section>

<!-- SLIDE 3: The Core Question -->
<section>
  <h2>The Core Question</h2>
  <p style="font-size:1.3em; margin: 1em 0;">
    What determines whether a satellite
    <span class="highlight">stays in orbit</span>,
    <span class="warn">escapes into space</span>, or
    <span style="color:#ff6666;">crashes back down</span>?
  </p>
  <div class="fragment">
    <p>I explored this by building a simulator and testing <span class="highlight">6 000 different launches</span>.</p>
  </div>
  <div class="fragment">
    <p class="small">Spoiler: it comes down to just two numbers &mdash; speed and direction.</p>
  </div>
  <aside class="notes">This is the central question of the thesis. I built a full simulator to answer it, and tested thousands of different scenarios systematically.</aside>
</section>

<!-- SLIDE 4: Ball-on-a-Hill Analogy -->
<section>
  <h2>Think of It Like a Ball on a Hill</h2>
  <p>Imagine rolling a ball up a hill:</p>
  <ul>
    <li class="fragment"><span class="highlight">Gentle push</span> &rarr; rolls partway up, comes back<br><span class="small">(this is an elliptical orbit)</span></li>
    <li class="fragment"><span class="warn">Exact right push</span> &rarr; barely reaches the top, stops<br><span class="small">(this is the escape boundary)</span></li>
    <li class="fragment"><span style="color:#ff6666;">Hard push</span> &rarr; flies over the top and keeps going<br><span class="small">(this is an escape trajectory)</span></li>
  </ul>
  <p class="fragment" style="margin-top:1em;">Gravity is the hill. Speed is the push.<br>
  <span class="highlight">Energy</span> decides which outcome you get.</p>
  <aside class="notes">This analogy is not just a metaphor. It is mathematically the same equation. The ball's kinetic energy minus the hill's potential energy determines the outcome. We will see the formula for this in a moment, but the intuition is: energy decides everything.</aside>
</section>

<!-- ============================================================ -->
<!-- ACT 2: HOW WE SOLVE IT                                       -->
<!-- ============================================================ -->

<!-- SLIDE 5: Gravity -->
<section>
  <h2>Gravity: The Only Force</h2>
  <p style="font-size:1.1em;">In space, there is no air resistance, no friction &mdash; just gravity pulling you toward the planet.</p>
  <div class="fragment">
    <p>The closer you are, the <span class="highlight">stronger the pull</span>.</p>
    <p>Twice as close = <span class="highlight">four times the force</span>.</p>
  </div>
  <div class="fragment">
    <div class="formula">F = G &middot; M &middot; m / r&sup2;</div>
    <p class="small">Newton's law of gravitation &mdash; the force between two masses, decreasing with the square of the distance.</p>
  </div>
  <aside class="notes">This is the only equation governing the entire simulation. Everything else follows from this one law. The inverse-square relationship means gravity weakens rapidly with distance, but never truly reaches zero.</aside>
</section>

<!-- SLIDE 6: Energy Decides the Orbit Type -->
<section>
  <h2>Energy Decides Everything</h2>
  <p>Remember the ball on the hill? We can calculate the <span class="highlight">total energy</span>:</p>
  <div class="fragment">
    <div class="formula">&epsilon; = v&sup2;/2 &minus; &mu;/r</div>
    <p class="small">&epsilon; = specific energy &nbsp;|&nbsp; v = speed &nbsp;|&nbsp; &mu; = G&middot;M &nbsp;|&nbsp; r = distance from center</p>
  </div>
  <div class="fragment">
    <p style="margin-top:0.5em;">The sign of &epsilon; tells us the outcome:</p>
    <ul>
      <li><span class="highlight">&epsilon; &lt; 0</span> &rarr; Not enough energy to escape &rarr; <strong>Elliptical orbit</strong></li>
      <li><span class="warn">&epsilon; = 0</span> &rarr; Just barely enough &rarr; <strong>Escape boundary</strong></li>
      <li><span style="color:#ff6666;">&epsilon; &gt; 0</span> &rarr; More than enough &rarr; <strong>Flies away forever</strong></li>
    </ul>
  </div>
  <p class="fragment small" style="margin-top:0.5em;">At 600 km altitude: circular orbit needs 7 561 m/s, escape needs 10 693 m/s</p>
  <aside class="notes">This connects back to the ball analogy. Negative energy means the ball does not have enough energy to leave the valley. Zero means it barely makes it to the top. Positive means it flies over.</aside>
</section>

<!-- SLIDE 7: Why Numerical Methods -->
<section>
  <h2>A Problem Computers Must Solve</h2>
  <p style="font-size:1.1em;">We know gravity's formula. Why can't we just solve it with pen and paper?</p>
  <div class="fragment">
    <p>For a perfect circle &mdash; we can. But for any realistic orbit:</p>
    <ul>
      <li>The force <span class="highlight">changes direction and strength</span> at every point</li>
      <li>Position depends on velocity, which depends on acceleration, which depends on position...</li>
    </ul>
  </div>
  <div class="fragment">
    <p style="margin-top:0.5em;">Solution: <span class="highlight">take tiny steps forward in time</span> and recalculate at each step.</p>
    <p class="small">This is called <strong>numerical integration</strong> &mdash; letting the computer trace the orbit step by step.</p>
  </div>
  <aside class="notes">Think of it like GPS navigation. Your phone does not calculate the entire route at once. It recalculates your position every second based on where you are NOW. Numerical integration works the same way.</aside>
</section>

<!-- SLIDE 8: Euler vs RK4 -->
<section>
  <h2>Two Ways to Take Those Steps</h2>
  <div class="two-col">
    <div>
      <h3>Euler's Method</h3>
      <p><span class="highlight">Look once</span>, step forward.</p>
      <div class="analogy-box">Like checking the weather only at midnight and assuming it stays the same all day.</div>
      <p class="fragment warn" style="margin-top:0.5em;">Problem: errors build up. The satellite slowly spirals away from its true path.</p>
    </div>
    <div>
      <h3>Runge-Kutta 4 (RK4)</h3>
      <p><span class="highlight">Look four times</span>, average the views, then step.</p>
      <div class="analogy-box">Like checking the weather at midnight, 6 AM, noon, and 6 PM, then planning your day.</div>
      <p class="fragment highlight" style="margin-top:0.5em;">Result: dramatically more accurate for the same step size.</p>
    </div>
  </div>
  <p class="fragment small" style="margin-top:0.8em;">Technical detail: RK4 uses four slope estimates (k1&ndash;k4) weighted 1:2:2:1, matching a Taylor expansion to 4th order.</p>
  <aside class="notes">The key takeaway is that RK4 looks ahead multiple times before deciding where to step, while Euler just looks once. That simple difference makes RK4 billions of times more accurate, as we will see in the results.</aside>
</section>

<!-- ============================================================ -->
<!-- ACT 3: THE TOOL                                              -->
<!-- ============================================================ -->

<!-- SLIDE 9: OrbitLab -->
<section>
  <h2>The Program &mdash; OrbitLab</h2>
  <p>Built in Python with Pygame for real-time visualization</p>
  <ul>
    <li><span class="highlight">10 celestial bodies</span> &mdash; Earth, Mars, Jupiter, and more</li>
    <li><span class="highlight">7+ scenarios</span> per planet (circular, elliptical, escape, etc.)</li>
    <li>Toggle between <span class="highlight">RK4</span> and <span class="warn">Euler</span> in real-time to see the difference</li>
    <li>Automated <span class="highlight">data logging</span> &amp; analysis for every run</li>
  </ul>
  <p class="fragment small" style="margin-top:1em;">Let me show you...</p>
  <aside class="notes">This is the program I built from scratch. Let me switch to a live demo so you can see it in action.</aside>
</section>

<!-- SLIDE 10: Demo placeholder -->
<section data-background-color="#000">
  <h2>Live Demo</h2>
  <p style="font-size:1.5em;">Switch to OrbitLab now</p>
  <p class="small">Run: <code>python src/main.py --demo</code></p>
  <p class="small">or run normally and demonstrate manually</p>
</section>

<!-- ============================================================ -->
<!-- ACT 4: RESULTS                                               -->
<!-- ============================================================ -->

<!-- SLIDE 11: Elliptical Orbit Result -->
<section>
  <h2>Result: Elliptical Orbit</h2>
  <div class="two-col">
    <div>
      <img src="{orbit_elliptical}" alt="Elliptical orbit">
    </div>
    <div>
      <ul>
        <li>Start: 600 km altitude, v = 8 696 m/s</li>
        <li>The satellite traces a <span class="highlight">closed ellipse</span></li>
        <li>Earth sits at one focus &mdash; exactly as <span class="highlight">Kepler predicted</span> 400 years ago</li>
        <li class="fragment">Period: ~10 400 s (~2 h 53 min)</li>
      </ul>
      <p class="fragment small" style="margin-top:0.5em;">The simulation rediscovered Kepler's 1st law purely from Newton's gravity equation &mdash; no ellipse was hard-coded.</p>
    </div>
  </div>
  <aside class="notes">This is a key result. The elliptical shape was not programmed in. It emerged naturally from Newton's gravity equation alone. The simulation independently confirmed what Kepler observed 400 years ago.</aside>
</section>

<!-- SLIDE 12: Escape Trajectory Result -->
<section>
  <h2>Result: Escape Trajectory</h2>
  <div class="two-col">
    <div>
      <img src="{orbit_escape}" alt="Escape trajectory">
    </div>
    <div>
      <ul>
        <li>Same altitude, but v = 11 500 m/s</li>
        <li>The satellite <span style="color:#ff6666;">never comes back</span></li>
        <li>Just <span class="highlight">33% more speed</span> &rarr; completely different outcome</li>
      </ul>
      <p class="fragment" style="margin-top:0.5em;">This is exactly how interplanetary missions work &mdash; <span class="highlight">Voyager 1</span> used this principle to leave the solar system.</p>
    </div>
  </div>
  <aside class="notes">Compare this to the previous slide. A relatively small change in speed, about 33 percent, is the difference between orbiting forever and escaping forever. This is the entire thesis visualized in two images.</aside>
</section>

<!-- SLIDE 13: Energy Conservation -->
<section>
  <h2>Result: Energy Conservation</h2>
  <div class="two-col">
    <div>
      <img src="{energy_rk4}" alt="RK4 energy">
      <p class="comparison-label"><span class="highlight">RK4</span></p>
    </div>
    <div>
      <img src="{energy_euler}" alt="Euler energy">
      <p class="comparison-label"><span class="warn">Euler</span></p>
    </div>
  </div>
  <div class="fragment" style="margin-top:0.5em;">
    <p>RK4 energy drift: 0.0000000000000181 &nbsp;&mdash;&nbsp; Euler drift: 0.00223</p>
    <p style="margin-top:0.3em;">RK4 is <span class="highlight">~100 billion times</span> more accurate.</p>
  </div>
  <p class="fragment small">Analogy: If Euler misses a target by 1 km, RK4 misses by the width of an atom.</p>
  <aside class="notes">These graphs show how well each method conserves energy over time. The flat line on the left means RK4 keeps energy almost perfectly constant. The drifting line on the right shows Euler slowly losing accuracy. The difference is staggering: 100 billion times.</aside>
</section>

<!-- SLIDE 14: Parameter Sweep -->
<section>
  <h2>Result: 6 000 Launches in One Image</h2>
  <div class="two-col">
    <div>
      <img src="{sweep_heatmap}" alt="Parameter sweep heatmap" style="max-height:50vh;">
    </div>
    <div>
      <p>Each pixel = one simulation with different speed + direction</p>
      <ul>
        <li><span style="color:#4CAF50;">Green</span> = stays in orbit (elliptical)</li>
        <li><span style="color:#FFC107;">Yellow</span> = right at the boundary</li>
        <li><span style="color:#f44336;">Red</span> = escapes into space</li>
      </ul>
      <p class="fragment" style="margin-top:0.5em;">The sharp boundary at <span class="highlight">~10 693 m/s</span> matches the theoretical escape velocity <strong>exactly</strong>.</p>
      <p class="fragment small">Notice: the angle barely matters &mdash; it is almost entirely about speed.</p>
    </div>
  </div>
  <aside class="notes">This is perhaps the most impressive result. 6000 simulations, each with different initial speed and direction, all plotted as a single heatmap. The sharp color boundary exactly where theory predicts is a strong confirmation that the simulation is correct.</aside>
</section>

<!-- ============================================================ -->
<!-- ACT 5: REFLECTION                                            -->
<!-- ============================================================ -->

<!-- SLIDE 15: Discussion -->
<section>
  <h2>Discussion</h2>
  <div class="two-col">
    <div>
      <h3>Key Findings</h3>
      <ul>
        <li>Escape velocity at 600 km matches theory exactly (10 693 m/s)</li>
        <li>RK4 conserves energy 10<sup>11</sup>&times; better than Euler</li>
        <li>Kepler's laws emerge naturally from Newton's gravity &mdash; not coded in</li>
        <li class="fragment">Numerical simulation can model physics where exact solutions are impractical</li>
      </ul>
    </div>
    <div>
      <h3>Limitations</h3>
      <ul>
        <li>2D simulation only (real orbits are 3D)</li>
        <li>Two bodies (no Moon, Sun, atmosphere)</li>
        <li>No relativistic effects</li>
      </ul>
      <p class="fragment small" style="margin-top:0.5em;">These limitations are well-understood and do not affect the core conclusions for this scope.</p>
    </div>
  </div>
  <aside class="notes">The results are confirmatory: they match established theory exactly. This is the expected outcome but it validates that the simulation and numerical methods are implemented correctly.</aside>
</section>

<!-- SLIDE 16: Challenges -->
<section>
  <h2>Challenges Along the Way</h2>
  <div class="challenge-card">
    <strong>The math was hard</strong><br>
    Understanding Taylor series, RK4 derivation, and orbital mechanics formulas took significant effort.
  </div>
  <div class="challenge-card fragment">
    <strong>Where do you even start?</strong><br>
    Going from "I want to simulate orbits" to actual working code required breaking the problem into small, manageable pieces.
  </div>
  <div class="challenge-card fragment">
    <strong>Debugging physics simulations</strong><br>
    When the orbit looks wrong, is it a code bug or a math bug? Hard to tell without systematic testing.
  </div>
  <div class="challenge-card fragment">
    <strong>Balancing ambition with time</strong><br>
    Wanting to add more features vs. actually finishing the project and report.
  </div>
  <aside class="notes">These are honest reflections on the process. Every one of these challenges taught me something valuable about problem-solving and project management.</aside>
</section>

<!-- SLIDE 17: Tips -->
<section>
  <h2>Tips for Your Gymnasiearbete</h2>
  <div class="tip-card">
    <strong>Start early &amp; don't procrastinate</strong><br>
    The project always takes longer than you think. Give yourself buffer time.
  </div>
  <div class="tip-card fragment">
    <strong>Choose something you actually enjoy</strong><br>
    You'll spend many hours on this. If the topic excites you, the work feels less like work.
  </div>
  <div class="tip-card fragment">
    <strong>Break big tasks into small steps</strong><br>
    "Build an orbit simulator" is overwhelming. "Calculate gravity between two points" is doable.
  </div>
  <div class="tip-card fragment">
    <strong>Use version control (Git)</strong><br>
    Save your progress, track changes, and never lose work. It's worth learning.
  </div>
  <div class="tip-card fragment">
    <strong>Don't be afraid to ask for help</strong><br>
    Teachers, classmates, online resources &mdash; nobody does it completely alone.
  </div>
  <aside class="notes">These are things I wish someone had told me at the start. Especially breaking big tasks into small steps — that was the single most useful skill I developed during this project.</aside>
</section>

<!-- SLIDE 18: Questions -->
<section data-background-color="#0a1225">
  <h1 style="font-size:3em;">Questions?</h1>
  <p style="margin-top:1em; font-size:0.95em;">I can also run any scenario live in OrbitLab.</p>
  <p class="small" style="margin-top:2em;">OrbitLab source code available on GitHub</p>
  <aside class="notes">Open the floor for questions. Offer to demonstrate specific scenarios live if anyone is curious about a particular orbit type or comparison.</aside>
</section>

</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/notes/notes.js"></script>
<script>
  Reveal.initialize({{
    hash: true,
    slideNumber: true,
    transition: 'slide',
    backgroundTransition: 'fade',
    center: true,
    width: 1280,
    height: 720,
    plugins: [RevealNotes]
  }});
</script>
</body>
</html>
"""

html = HTML_TEMPLATE.format(**imgs)

output_path = os.path.join(SCRIPT_DIR, "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Created {output_path} ({len(html):,} bytes)")
