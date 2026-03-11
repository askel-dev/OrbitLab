#!/usr/bin/env python3
"""
Local build script for creating distributable executables.
Run this before creating a release to test the build process locally.

Usage:
    python build_local.py

Requirements:
    pip install pyinstaller pillow
"""

import os
import sys
import platform
import subprocess
from pathlib import Path


def main():
    """Build executable for current platform"""
    print("=" * 60)
    print("Building Orbital Simulator")
    print("=" * 60)

    # Detect platform
    system = platform.system()
    print(f"Platform: {system}")

    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("ERROR: PyInstaller not found!")
        print("Install it with: pip install pyinstaller")
        sys.exit(1)

    # Read version from version.txt
    version_file = Path("version.txt")
    version = version_file.read_text().strip() if version_file.exists() else "0.1.0"
    print(f"Version: {version}")

    # Generate icon assets
    print("\nGenerating app icon...")
    try:
        subprocess.run([sys.executable, "src/generate_icon.py"], check=True)
    except subprocess.CalledProcessError:
        print("Warning: icon generation failed — using fallback")

    # Build configuration
    name = f"OrbitalSimulator-v{version}"
    main_file = "src/main.py"
    icon_win = "assets/icon.ico"
    icon_other = "assets/icon.png"

    # Common PyInstaller arguments
    args = [
        "pyinstaller",
        "--clean",  # Clean cache
        "--name", name,
        "--add-data", f"assets{os.pathsep}assets",  # Include assets folder
    ]

    # Platform-specific arguments
    if system == "Windows":
        args.extend([
            "--onefile",
            "--windowed",
            f"--icon={icon_win}",
        ])
    elif system == "Darwin":  # macOS
        args.extend([
            "--onefile",
            "--windowed",
            f"--icon={icon_other}",
        ])
    elif system == "Linux":
        args.extend([
            "--onefile",
            f"--icon={icon_other}",
        ])

    # Add main file
    args.append(main_file)

    print("\nBuild command:")
    print(" ".join(args))
    print("\nBuilding... (this may take a few minutes)")
    print("-" * 60)

    # Run PyInstaller
    try:
        subprocess.run(args, check=True)
        print("-" * 60)
        print("\n✅ Build successful!")
        print(f"\nExecutable location: dist/{name}")

        if system == "Windows":
            print(f"  → dist/{name}.exe")
        elif system == "Darwin":
            print(f"  → dist/{name}.app (or .dmg if packaged)")
        else:
            print(f"  → dist/{name}")

        print("\nTest the executable before creating a release!")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed with error code {e.returncode}")
        sys.exit(1)


if __name__ == "__main__":
    main()
