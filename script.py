import sys
import venv
import subprocess
from pathlib import Path

# this script creates a project folder with:
# - pyproject.toml (modern PEP 621 metadata)
# - src/<project_name>/ pkg directoryy
# - a virtual environment with seed dependencies installed
# - a requirements.txt snapshot
# - tests/ directory
# - .gitignore

def create_project():
    current_dir = Path.cwd()

    project_name = input('Enter name for this project > ').strip().lower()
    if not project_name:
        print("Project name cannot be empty.")
        return

    project_path = current_dir / project_name
    venv_path = project_path / "venv"

    if project_path.exists():
        print(f"error: {project_name} already exists at {project_path}. Exiting.")
        sys.exit(1)

    project_path.mkdir(parents=True)
    print(f"created project folder: {project_path}")

    # write pyproject.toml 
    pyproject_content = f"""[build-system]
requires = ["setuptools>=64"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "0.1.0"
description = ""
readme = "README.md"
requires-python = ">=3.8"
dependencies = []
"""
    (project_path / "pyproject.toml").write_text(pyproject_content)

    # write .gitignore 
    gitignore_content = """venv/
__pycache__/
*.pyc
*.pyo
.env
dist/
*.egg-info/
.pytest_cache/
.mypy_cache/
.ruff_cache/
"""
    (project_path / ".gitignore").write_text(gitignore_content)

    # create <src>/<project_name>/<package> 
    src_pkg = project_path / "src" / project_name
    src_pkg.mkdir(parents=True)
    (src_pkg / "__init__.py").write_text(f'__version__ = "0.1.0"\n')

    # create tests/ directory 
    tests_dir = project_path / "tests"
    tests_dir.mkdir()
    (tests_dir / "__init__.py").write_text("")
    test_content = f'''from {project_name} import __version__


def test_version():
    assert __version__ == "0.1.0"
'''
    (tests_dir / f"test_{project_name}.py").write_text(test_content)

    # create virtual environment
    print("Installing virtual environment...")
    venv.EnvBuilder(with_pip=True).create(venv_path)

    # determine python executable (cross-platform)
    python_exe = venv_path / ("Scripts" if sys.platform == "win32" else "bin") / "python"

    try:
        sys.stdout.flush()
        print("Upgrading pip...")
        sys.stdout.flush()
        subprocess.run([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"], check=True)

        sys.stdout.flush()
        seed_reqs = Path("requirements.txt")
        if seed_reqs.exists():
            print(f"Installing dependencies from {seed_reqs.absolute()}...")
            sys.stdout.flush()
            subprocess.run([str(python_exe), "-m", "pip", "install", "-r", str(seed_reqs)], check=True)

        sys.stdout.flush()
        print("Installing project in editable mode...")
        sys.stdout.flush()
        subprocess.run([str(python_exe), "-m", "pip", "install", "-e", str(project_path)], check=True)

        sys.stdout.flush()
        print("Generating requirements.txt snapshot...")
        sys.stdout.flush()
        result = subprocess.run(
            [str(python_exe), "-m", "pip", "freeze"],
            capture_output=True, text=True, check=True
        )
        (project_path / "requirements.txt").write_text(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during installation: {e}")
        sys.exit(1)

    print("-" * 30)
    print(f"Project '{project_name}' initialized successfully.")
    print(f"Location: {project_path}")
    print(f"To activate: {'source venv/bin/activate' if sys.platform != 'win32' else 'venv\\Scripts\\activate'}")


if __name__ == "__main__":
    create_project()
