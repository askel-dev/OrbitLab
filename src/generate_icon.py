#!/usr/bin/env python3
"""
Generate app icon for OrbitLab.

Produces:
  assets/icon.png  — 512x512 PNG (used for macOS and as source)
  assets/icon.ico  — multi-size ICO (16, 32, 48, 64, 128, 256 px) for Windows

Requires: matplotlib, pillow
  pip install pillow
"""

import os
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Ellipse, Circle


ASSETS_DIR = Path(__file__).parent.parent / "assets"

# --- colours ---
BG_COLOR       = "#0a0a1a"   # deep space navy
PLANET_COLOR   = "#2255cc"   # blue planet
PLANET_SHADE   = "#112266"   # dark rim
ATMOSPHERE     = "#4488ff"   # soft glow ring
ORBIT_COLOR    = "#ffffff"   # orbit line
SAT_COLOR      = "#ffffff"   # satellite dot
STAR_COLOR     = "#ccddff"   # background stars


def _add_stars(ax, rng, n=120):
    xs = rng.uniform(-1, 1, n)
    ys = rng.uniform(-1, 1, n)
    sizes = rng.uniform(0.3, 2.5, n)
    alphas = rng.uniform(0.3, 0.9, n)
    for x, y, s, a in zip(xs, ys, sizes, alphas):
        ax.plot(x, y, "o", color=STAR_COLOR, markersize=s, alpha=a)


def generate_icon_png(path: Path, size: int = 512):
    fig, ax = plt.subplots(figsize=(1, 1), dpi=size)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    rng = np.random.default_rng(42)
    _add_stars(ax, rng)

    # orbit ellipse (draw first so planet sits on top)
    orbit = Ellipse(
        xy=(0.0, 0.0),
        width=1.30,
        height=0.55,
        angle=-15,
        fill=False,
        edgecolor=ORBIT_COLOR,
        linewidth=1.2,
        alpha=0.85,
        zorder=2,
    )
    ax.add_patch(orbit)

    # atmosphere glow (slightly larger circle, transparent)
    atm = Circle((-0.05, -0.05), 0.35, color=ATMOSPHERE, alpha=0.12, zorder=3)
    ax.add_patch(atm)

    # planet body
    planet = Circle((-0.05, -0.05), 0.30, color=PLANET_COLOR, zorder=4)
    ax.add_patch(planet)

    # subtle dark rim on planet
    rim = Circle((-0.05, -0.05), 0.30, fill=False, edgecolor=PLANET_SHADE,
                 linewidth=2.5, alpha=0.6, zorder=5)
    ax.add_patch(rim)

    # satellite dot on orbit (upper-right arc)
    # parametric point on the ellipse at ~40 degrees
    a, b, theta_rot = 0.65, 0.275, np.radians(-15)
    t = np.radians(40)
    sx = a * np.cos(t) * np.cos(theta_rot) - b * np.sin(t) * np.sin(theta_rot)
    sy = a * np.cos(t) * np.sin(theta_rot) + b * np.sin(t) * np.cos(theta_rot)
    sat = Circle((sx, sy), 0.045, color=SAT_COLOR, zorder=6)
    ax.add_patch(sat)

    fig.savefig(path, dpi=size, bbox_inches="tight", pad_inches=0,
                facecolor=BG_COLOR)
    plt.close(fig)
    print(f"  Saved {path}")


def generate_icon_ico(png_path: Path, ico_path: Path):
    try:
        from PIL import Image
    except ImportError:
        print("  Pillow not found — skipping .ico generation")
        print("  Install with: pip install pillow")
        return

    img = Image.open(png_path).convert("RGBA")
    sizes = [16, 32, 48, 64, 128, 256]
    resized = [img.resize((s, s), Image.LANCZOS) for s in sizes]
    resized[0].save(ico_path, format="ICO", sizes=[(s, s) for s in sizes],
                    append_images=resized[1:])
    print(f"  Saved {ico_path}")


def main():
    ASSETS_DIR.mkdir(exist_ok=True)
    png_path = ASSETS_DIR / "icon.png"
    ico_path = ASSETS_DIR / "icon.ico"

    print("Generating app icon...")
    generate_icon_png(png_path)
    generate_icon_ico(png_path, ico_path)
    print("Done.")


if __name__ == "__main__":
    main()
