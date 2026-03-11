# 🚀 Quick Start: Your First Release

This is a condensed guide to get your first release out ASAP!

## 📝 Pre-Flight Checklist (5 minutes)

- [ ] Add your splash screen feature
- [ ] Test that everything works
- [ ] Commit and push all changes
- [ ] Update CHANGELOG.md (move items from Unreleased to v1.0.0)

## 🎯 The Fast Path (Automated Build)

### Step 1: Commit Everything
```bash
git add .
git commit -m "feat: add splash screen for v1.0.0 release"
git push origin main
```

### Step 2: Create and Push Tag
```bash
git tag -a v1.0.0 -m "Release v1.0.0 - First stable release"
git push origin v1.0.0
```

### Step 3: Wait for Magic ✨
- Go to your GitHub repository
- Click "Actions" tab
- Watch the workflow build Windows .exe and macOS .zip (5-15 min)
- When done, go to "Releases" tab
- Edit the draft release if needed
- Click "Publish release"

**Done!** 🎉

---

## 🧪 Test Locally First (Optional but Recommended)

Before pushing the tag, test the build:

```bash
# Install PyInstaller
pip install pyinstaller

# Build locally
python build_local.py

# Test the executable in dist/ folder
```

---

## 📋 What Files Were Created

| File | Purpose |
|------|---------|
| `.github/workflows/release.yml` | Automates building .exe and .zip on GitHub |
| `CHANGELOG.md` | Track changes between versions |
| `RELEASE_GUIDE.md` | Complete guide (read this for details!) |
| `build_local.py` | Build executables on your machine |
| `version.txt` | Track current version |
| `QUICK_START_RELEASE.md` | This file! |

---

## 🎨 Customize Release Notes

When the release is created, edit it to include:

```markdown
## 🎯 What's New in v1.0.0

### ✨ New Features
- 🖼️ Beautiful splash screen on startup
- [Your other features]

### 📦 Download Instructions

**Windows:**
1. Download the .exe file
2. Run it (click "More info" → "Run anyway" if Windows warns)

**macOS:**
1. Download the .zip file
2. Extract and right-click → Open (first time)
```

---

## ⚠️ Common Issues

### "Windows Defender blocked this app"
**Normal!** Unsigned apps trigger this. Tell users:
1. Click "More info"
2. Click "Run anyway"

### "macOS can't verify developer"
**Normal!** Tell users to right-click → Open (not double-click)

### Build fails in GitHub Actions
- Check the Actions tab for error logs
- Usually missing dependencies or path issues
- Fix and push a new tag: `v1.0.1`

---

## 🎓 Next Steps

1. **After release:** Monitor GitHub Issues for bug reports
2. **For v1.1.0:** Add new features based on feedback
3. **Read:** `RELEASE_GUIDE.md` for comprehensive details

---

## 🆘 Need Help?

- **Full guide:** Read `RELEASE_GUIDE.md`
- **Versioning:** Read `CHANGELOG.md` format
- **Build issues:** Check PyInstaller docs
- **GitHub Actions:** Check `.github/workflows/release.yml` comments

**You've got this!** 🚀
