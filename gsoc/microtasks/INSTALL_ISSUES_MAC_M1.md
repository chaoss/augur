
# 🛠 Microtask 2: Installation Issues Encountered on macOS 14.4 (M1)

This document outlines the issues I encountered while installing [CHAOSS Augur](https://github.com/chaoss/augur) on a **macOS 14.4 M1** machine using **Python 3.9.18** and **Augur v0.86.0**, along with the solutions I applied to resolve them.

---

### ❗️Issue 1: pyenv under Rosetta 2
**Problem:**  
Using `pyenv` to install Python 3.8.x failed due to Rosetta architecture issues:
```
Error: Cannot install under Rosetta 2 in ARM default prefix (/opt/homebrew)!
```

**Solution:**  
Force Homebrew and pyenv to run natively on ARM:
```bash
arch -arm64 pyenv install 3.8.17
```
Or with full flags:
```bash
CFLAGS="-I$(brew --prefix zlib)/include -I$(brew --prefix bzip2)/include" \
LDFLAGS="-L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" \
PYTHON_CONFIGURE_OPTS="--enable-framework" \
arch -arm64 pyenv install 3.8.17
```

---

### ❗️Issue 2: Python 3.8 not compatible with macOS 14
**Problem:**  
Even after installing Python 3.8, some packages like `numpy==1.26.0` and `tensorflow` failed to compile or install properly.

**Solution:**  
Upgrade to Python 3.9:
```bash
arch -arm64 pyenv install 3.9.18
pyenv global 3.9.18
```

---

### ❗️Issue 3: `make install-dev` does not exist
**Problem:**  
The official documentation suggests:
```bash
make install-dev
```
But the Makefile doesn’t have this target.

**Solution:**  
Run the regular install command:
```bash
make install
```

---

### ❗️Issue 4: `.git-credentials` permission error
**Problem:**  
During configuration, Augur attempts to create `.git-credentials` in `/`, which fails:
```
touch: /.git-credentials: Read-only file system
```

**Solution:**  
Create a Facade repo directory manually before running the install:
```bash
mkdir -p ~/augur/repos
```
Then use the full path when prompted:
```
Facade worker directory: /Users/<yourname>/augur/repos
```

---

### ❗️Issue 5: `h5py` version conflict with TensorFlow
**Problem:**  
`augur` installs `h5py==3.10.0` but `tensorflow>=2.19.0` requires `h5py>=3.11.0`:
```
tensorflow 2.19.0 requires h5py>=3.11.0, but you have h5py 3.10.0
```

**Solution:**  
Manually install the required version:
```bash
pip install 'h5py>=3.11.0'
```
⚠️ Warning: This conflicts with Augur’s `setup.py`. It may be necessary to fork and patch `requirements.txt`.

---

### ❗️Issue 6: Invalid CLI commands in docs (`augur db init`)
**Problem:**  
Documentation suggests running:
```bash
augur db init
```
But this returns:
```
Error: No such command 'init'
```

**Solution:**  
Use the actual CLI options:
```bash
augur db init-database        # if database doesn't exist
augur db create-schema        # to create schema
augur db upgrade-db-version   # to apply migrations
```

---

### ❗️Issue 7: NLTK download prompt
**Problem:**  
During installation, Augur prompts:
```
Would you like to install required NLTK word lists for machine learning workers?
```

**Solution:**  
Accept prompt by typing `y`, or manually install later with:
```python
import nltk
nltk.download('all')
```

---

## ✅ Summary

These issues are frequently encountered during Augur installation on Apple Silicon Macs. Resolving and documenting them helps improve onboarding and reduces developer friction.

---

**System Info:**  
- macOS 14.4 (M1)  
- Python 3.9.18 (via pyenv)  
- Augur v0.86.0  
- RabbitMQ, PostgreSQL, Redis installed via Homebrew  
- Virtualenv: `augur39`

---

Maintained by [Xiaoha](mailto:placeholder@email.com)
```