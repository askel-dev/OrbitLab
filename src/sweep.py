"""Parametersvep som klassificerar bantyper för olika startförhållanden (analytiskt eller simulerat)."""
from __future__ import annotations

import math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from physics import G, M_EARTH, MU_EARTH, EARTH_RADIUS, get_acceleration, rk4_step

# Använd jordens konstanter
M = M_EARTH
MU = MU_EARTH

# ===========================
# FYSIKALISKA KONSTANTER
# ===========================
R0 = np.array([7_000_000.0, 0.0])  # Startavstånd: 7000 km från jordens centrum

# ===========================
# SVEPINSTÄLLNINGAR
# ===========================
SPEED_RANGE = (6_500.0, 12_500.0)   # m/s
ANGLE_RANGE = (0.0, math.pi / 2.0)  # radianer
SPEED_POINTS = 300                  # horisontell upplösning (x-axel)
ANGLE_POINTS = 20                   # vertikal upplösning (y-axel)

MODE = "simulated"       # "fast" = analytisk (1 sek), "simulated" = RK4 (långsammare)
DT = 10.0
MAX_STEPS = 600
ESCAPE_RADIUS_FACTOR = 8.0

ENERGY_TOL = 3e5  # ±300 000 J/kg -> synlig gul zon

FIGURES_DIR = Path("figures")

# ===========================
# FYSIKALISKA HJÄLPFUNKTIONER
# ===========================
def energy_specific(r: np.ndarray, v: np.ndarray) -> float:
    rmag = math.hypot(r[0], r[1])
    vmag2 = v[0]**2 + v[1]**2
    return 0.5 * vmag2 - MU / rmag

# ===========================
# KLASSIFICERING
# ===========================
def classify_fast(speed: float) -> int:
    """Klassificera bantyp baserat på startenergi."""
    eps0 = 0.5 * speed**2 - MU / np.linalg.norm(R0)
    if eps0 < -ENERGY_TOL:
        return 0  # Elliptisk
    elif eps0 > ENERGY_TOL:
        return 2  # Hyperbolisk
    else:
        return 1  # Parabolisk (inom ±ENERGY_TOL)

def classify_simulated(speed: float, angle_rad: float, escape_radius: float) -> int:
    """Numerisk RK4-integration för klassificering."""
    r = R0.copy()
    v = np.array([speed * math.cos(angle_rad), speed * math.sin(angle_rad)])
    for _ in range(MAX_STEPS):
        r, v = rk4_step(r, v, DT)
        rmag = math.hypot(r[0], r[1])
        if rmag <= EARTH_RADIUS:
            return 3  # Krasch
        eps = energy_specific(r, v)
        if eps > 0.0 and rmag > escape_radius:
            return 2
    eps = energy_specific(r, v)
    if eps < -ENERGY_TOL:
        return 0
    elif eps > ENERGY_TOL:
        return 2
    else:
        return 1

# ===========================
# HUVUDSVEP
# ===========================
def run_sweep() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    speeds = np.linspace(*SPEED_RANGE, SPEED_POINTS)
    angles = np.linspace(*ANGLE_RANGE, ANGLE_POINTS)
    escape_radius = ESCAPE_RADIUS_FACTOR * np.linalg.norm(R0)
    results = np.zeros((angles.size, speeds.size), dtype=int)

    total = angles.size * speeds.size
    print(f"\n--- Kör parameter-svep ({MODE}) ---")
    print(f"Totalt {total} punkter ({SPEED_POINTS} hastigheter × {ANGLE_POINTS} vinklar)")

    processed = 0
    for i, angle in enumerate(angles):
        for j, speed in enumerate(speeds):
            if MODE == "fast":
                results[i, j] = classify_fast(speed)
            else:
                results[i, j] = classify_simulated(speed, angle, escape_radius)
            processed += 1
        if i % 2 == 0:
            pct = 100 * processed / total
            print(f"  {i+1}/{angles.size} rader klara ({pct:.1f}%)")

    return speeds, angles, results

# ===========================
# VISUALISERING
# ===========================
def plot_heatmap(speeds: np.ndarray, angles: np.ndarray, results: np.ndarray) -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    cmap = ListedColormap(["#2f9e44", "#ffd43b", "#f03e3e", "#868e96"])  # grön, gul, röd, grå

    fig, ax = plt.subplots(figsize=(10, 6))
    extent = [speeds.min(), speeds.max(), math.degrees(angles.min()), math.degrees(angles.max())]
    im = ax.imshow(results, origin="lower", extent=extent, aspect="auto",
                   cmap=cmap, vmin=-0.5, vmax=3.5)
    cbar = fig.colorbar(im, ticks=[0,1,2,3])
    cbar.ax.set_yticklabels(["Ellips", "Parabel", "Hyperbel", "Krasch"])
    ax.set_xlabel("Starthastighet [m/s]")
    ax.set_ylabel("Startvinkel [grader]")
    ax.set_title(f"Bantyp per starthastighet och vinkel ({MODE})")
    fig.tight_layout()
    out = FIGURES_DIR / f"sweep_heatmap_{MODE}.png"
    fig.savefig(out, dpi=180)
    plt.close(fig)
    print(f"\nHeatmap sparad till {out}")

# ===========================
# HUVUDPROGRAM
# ===========================
def main() -> None:
    v_esc = math.sqrt(2 * MU / np.linalg.norm(R0))
    print(f"Flykthastighet vid {np.linalg.norm(R0)/1000:.0f} km: {v_esc:.2f} m/s")
    print(f"Energitolerans: ±{ENERGY_TOL:.1e} J/kg")
    speeds, angles, results = run_sweep()
    plot_heatmap(speeds, angles, results)

if __name__ == "__main__":
    main()