# py-init

A lightweight automation script to bootstrap modern Python projects. It handles directory creation, virtual environments, dependency management, and project scaffolding — all with zero external dependencies.

---

### Features

- **Modern Standards**: Generates `pyproject.toml` (PEP 621) with `[build-system]` and uses `pathlib` for cross-platform stability.
- **Automated Venv**: Creates and updates a virtual environment automatically.
- **Seed Dependencies**: Installs packages from a local `requirements.txt` if present, then freezes a snapshot into the new project.
- **Project Scaffolding**: Creates a `src/` package layout, a `tests/` directory, and a `.gitignore`.
- **Zero-Config Pathing**: Operates in your current directory — no hardcoded paths.

---

### Usage

1. Place `script.py` in a convenient location.
2. (Optional) Place a `requirements.txt` next to the script with your default libraries (e.g., `requests`, `pytest`).
3. Run it:
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
├── venv/               # isolated virtual environment
├── pyproject.toml      # modern project metadata (PEP 621)
├── requirements.txt    # frozen dependency snapshot
└── .gitignore          # ignores venv, __pycache__, etc.
```

---

### License

MIT — see [LICENSE](LICENSE).

### Requirements

- Python 3.8+
- Compatible with Windows, macOS, and Linux.

Feedback is welcome — feel free to open a PR if you have ideas for improvements!
