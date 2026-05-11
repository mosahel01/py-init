## py-init

A lightweight automation script to bootstrap modern Python projects. It handles directory creation, virtual environments, and dependency management using current industry standards (pathlib and pyproject.toml).
✨ Features

    Zero-Config Pathing: Operates in your current directory—no hardcoded paths required.

    Modern Standards: Generates pyproject.toml and uses pathlib for cross-platform stability.

    Automated Venv: Creates and updates a virtual environment automatically.

    Seed Dependencies: Installs packages from a local requirements.txt if present.

🚀 Usage

    Placement: Keep py-init.py in your path or a dedicated scripts folder.

    (Optional): Place a requirements.txt next to the script containing your "default" libraries (e.g., requests, pytest).

    Run:
    Bash

    python py-init.py

    Follow Prompt: Enter your project name.

📂 Structure Created
Plaintext

your-project/
├── venv/              # Isolated virtual environment
├── pyproject.toml     # Modern project metadata
└── (requirements.txt) # Optional: seeded from script source

🛠️ Requirements

    Python 3.6+

    Compatible with Windows, macOS, and Linux.