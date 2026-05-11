# 🛠️ py-init

A lightweight automation script to bootstrap modern Python projects. It handles directory creation, virtual environments, and dependency management using current industry standards (`pathlib` and `pyproject.toml`).

---

### ✨ Features

*   **Zero-Config Pathing**: Operates in your current directory—no hardcoded paths required.
*   **Modern Standards**: Generates `pyproject.toml` and uses `pathlib` for cross-platform stability.
*   **Automated Venv**: Creates and updates a virtual environment automatically.
*   **Seed Dependencies**: Installs packages from a local `requirements.txt` if present.

---

### 🚀 Usage

1.  **Placement**: Keep `py-init.py` in your path or a dedicated scripts folder.
2.  **(Optional)**: Place a `requirements.txt` next to the script containing your "default" libraries (e.g., `requests`, `pytest`).
3.  **Run**:
    ```bash
    python py-init.py
    ```
