# 🐧 WSL2 & Windows: Environment Setup Troubleshooting Notes

These notes are based on installation errors encountered while setting up Augur on a Windows 11 + WSL2 system. They aim to assist new contributors in overcoming platform-specific issues and improving onboarding documentation.

---

## 🔧 Common Problems & Fixes

### 1. Shell scripts not executing (`.sh not found`)
**Symptoms**: Error like `install.sh: not found` or `permission denied`.

**Fix**:
```bash
dos2unix scripts/install/*.sh
chmod +x scripts/install/*.sh
