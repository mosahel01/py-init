# py-init

A lightweight automation script to bootstrap modern Python projects. It handles directory creation, virtual environments, dependency management, and project scaffolding — all with zero external dependencies.

---

### Features

- **Modern Standards**: generates `pyproject.toml` (PEP 621) with `[build-system]`, auto-detected `requires-python`, and dev dependencies (`pytest`, `ruff`).
- **Automated Venv**: creates and updates a virtual environment automatically.
- **Seed Dependencies**: installs packages from a local `requirements.txt` if present, then freezes a snapshot into the new project.
- **Project Scaffolding**: creates a `src/` package layout, `tests/` directory, `.gitignore`, and `.pre-commit-config.yaml`.
- **Zero-Config Pathing**: operates in your current directory — no hardcoded paths.

---

### Usage

1. place `script.py` in a convenient location.
2. (optional) Place a `requirements.txt` next to the script with your default libraries (e.g., `requests`, `pytest`).
3. Run:
   ```bash
   python script.py
   ```
4. Enter your project name when prompted.

---

### Generated Structure

```
your-project/
├── src/
│   └── your_project/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_your_project.py
├── venv/                    # isolated virtual environment
├── pyproject.toml           # project metadata + optional dev deps
├── requirements.txt         # frozen dependency snapshot
├── .gitignore               # ignores venv, __pycache__, etc.
└── .pre-commit-config.yaml  # ruff linter and formatter
```

---

### Requirements

- Python 3.8+
- Compatible with Windows, macOS, and Linux.

---

### License

MIT — see [LICENSE](LICENSE).

Feedback is welcome — feel free to open a PR if you have ideas for improvements!
