# 🚀 Release Management Guide

This guide walks you through creating and managing releases for the Orbital Simulator project.

## 📋 Table of Contents
1. [Pre-Release Checklist](#pre-release-checklist)
2. [Creating Your First Release](#creating-your-first-release)
3. [Automated vs Manual Builds](#automated-vs-manual-builds)
4. [Version Numbering](#version-numbering)
5. [Troubleshooting](#troubleshooting)

---

## Pre-Release Checklist

Before creating a release, ensure:

- [ ] All features are complete and tested
- [ ] Code is committed and pushed to main branch
- [ ] CHANGELOG.md is updated with new changes
- [ ] Version number is decided (following semantic versioning)
- [ ] Built and tested executables locally (optional but recommended)
- [ ] README.md reflects current features
- [ ] No known critical bugs

---

## Creating Your First Release

### Option 1: Automated Build (Recommended) ✨

This uses GitHub Actions to automatically build for Windows and macOS.

**Steps:**

1. **Update CHANGELOG.md**
   ```bash
   # Edit CHANGELOG.md and move unreleased items to new version section
   # Example: ## [1.0.0] - 2026-01-17
   ```

2. **Commit your changes**
   ```bash
   git add .
   git commit -m "chore: prepare release v1.0.0"
   git push origin main
   ```

3. **Create and push a version tag**
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0 - First stable release with splash screen"
   git push origin v1.0.0
   ```

4. **Wait for GitHub Actions** (5-15 minutes)
   - Go to your repository → Actions tab
   - Watch the "Build and Release" workflow run
   - It will automatically create Windows .exe and macOS .zip

5. **Review the draft release**
   - Go to repository → Releases
   - Edit the auto-generated release notes if needed
   - Click "Publish release"

**Done!** 🎉 Your release is live with downloadable binaries!

---

### Option 2: Manual Build

If you prefer to build locally:

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Run the local build script**
   ```bash
   python build_local.py
   ```

3. **Test the executable**
   - Find it in `dist/` folder
   - Run it and verify everything works
   - Test on a clean machine if possible (no Python installed)

4. **Create GitHub release manually**
   ```bash
   # Create tag
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0
   ```

5. **Upload binaries**
   - Go to GitHub → Releases → Draft a new release
   - Select your tag (v1.0.0)
   - Upload the executables from `dist/`
   - Write release notes (see template below)
   - Publish!

---

## Version Numbering

Follow [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`

### For Your Project:

| Version | When to Use | Example |
|---------|-------------|---------|
| **v0.1.0** | First working release (experimental) | Initial working simulator |
| **v0.2.0** | Add splash screen feature | After adding splash screen |
| **v1.0.0** | First stable release | When ready for public use |
| **v1.1.0** | Add new feature | Add new orbit types |
| **v1.1.1** | Bug fix | Fix crash on startup |
| **v2.0.0** | Breaking changes | Complete UI redesign |

**Recommendation for first release:** `v1.0.0` (if stable) or `v0.1.0` (if experimental)

---

## Release Notes Template

Use this template when creating releases:

```markdown
## 🎯 What's New in v1.0.0

### ✨ New Features
- 🖼️ Beautiful splash screen on startup
- [Other new features]

### 🔧 Improvements
- Improved rendering performance
- Better UI responsiveness
- [Other improvements]

### 🐛 Bug Fixes
- Fixed issue with [X]
- Resolved crash when [Y]

### 📦 Installation

#### Windows
1. Download `OrbitalSimulator-v1.0.0-windows.exe`
2. Run the .exe file
3. If Windows Defender warns you, click "More info" → "Run anyway"

#### macOS
1. Download `OrbitalSimulator-v1.0.0-macos.zip`
2. Extract the .zip file
3. Right-click the app → Select "Open" (first time only)
4. macOS will ask for permission, click "Open"

#### Linux / From Source
See [INSTALLATION.md](INSTALLATION.md) for instructions.

### 📊 System Requirements
- **Windows**: Windows 10 or later
- **macOS**: macOS 10.13 or later
- **Memory**: 512 MB RAM minimum
- **Display**: 1024x768 minimum resolution

### 🙏 Acknowledgments
[Thank contributors, libraries used, etc.]

---

**Full Changelog**: https://github.com/YOURUSERNAME/YOURREPO/compare/v0.1.0...v1.0.0
```

---

## Automated vs Manual Builds

### GitHub Actions (Automated) ✅ Recommended

**Pros:**
- ✅ Builds on clean environments (Windows + macOS)
- ✅ Consistent builds every time
- ✅ No need for macOS machine
- ✅ Automatic upload to releases
- ✅ Free for public repositories

**Cons:**
- ❌ Takes 5-15 minutes
- ❌ Requires GitHub Actions setup
- ❌ Need to troubleshoot remotely if issues

### Local Builds

**Pros:**
- ✅ Immediate feedback
- ✅ Easy to debug
- ✅ Full control

**Cons:**
- ❌ Need each OS to build for it (can't build macOS on Windows)
- ❌ Manual upload to GitHub
- ❌ Environment differences may cause issues

**Best Practice:** Test locally first, then use GitHub Actions for releases.

---

## Troubleshooting

### Windows Defender / Antivirus Flags

**Problem:** Windows flags your .exe as suspicious

**Solutions:**
1. **Code signing** (costs money ~$200/year)
   - Get a code signing certificate
   - Sign your .exe with `signtool`

2. **VirusTotal check** (free)
   - Upload to virustotal.com
   - Share the clean scan in release notes

3. **User instructions** (free)
   - Add clear instructions: "Click More Info → Run Anyway"
   - Explain this is common for unsigned apps

### macOS Gatekeeper Issues

**Problem:** macOS says "app can't be opened because it's from an unidentified developer"

**Solutions:**
1. **Notarization** (requires Apple Developer account - $99/year)
2. **User instructions** (free)
   - Tell users to right-click → Open
   - This bypasses Gatekeeper for trusted apps

### Build Fails - Missing Dependencies

**Problem:** PyInstaller doesn't include all files

**Solution:**
```bash
# Use --hidden-import for missing modules
pyinstaller --hidden-import=pygame --hidden-import=numpy src/main.py

# Use --collect-all for packages with data
pyinstaller --collect-all pygame src/main.py
```

### Large File Size

**Problem:** .exe is 200MB+ in size

**This is normal!** It includes:
- Python interpreter
- All libraries (Pygame, NumPy, etc.)
- Your code and assets

**To reduce size:**
- Use `--onefile` (already doing)
- Remove unused imports
- Compress with UPX: `pyinstaller --upx-dir=/path/to/upx`

---

## 📚 Additional Resources

- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [PyInstaller Documentation](https://pyinstaller.org/)
- [GitHub Releases Guide](https://docs.github.com/en/repositories/releasing-projects-on-github)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

## 🎓 Quick Reference Commands

```bash
# Create and push a release tag
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# Build locally (test)
python build_local.py

# List all tags
git tag -l

# Delete a tag (if you made a mistake)
git tag -d v1.0.0                    # Delete locally
git push origin --delete v1.0.0      # Delete on GitHub

# View last tag
git describe --tags --abbrev=0
```

---

## Next Steps After Your First Release

1. **Monitor issues** - Users will report bugs
2. **Plan v1.1.0** - Based on feedback
3. **Keep CHANGELOG updated** - For transparency
4. **Celebrate!** 🎉 - You shipped software!

---

**Good luck with your release!** 🚀
