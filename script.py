import sys
import venv
import subprocess
from pathlib import Path

# this script creates a project folder, install a venv, then install packages from a requirements.txt file.
# at the end it creates a requirements.txt inside the project for future collaborators to use.

def create_project():
    current_dir = Path.cwd() # this defaults to the current directory unless you provide a path
    
    project_name = input('Enter name for this project > ').strip().lower()
    if not project_name:
        print("Project name cannot be empty.")
        return

    project_path = current_dir / project_name
    venv_path = project_path / "venv"

    if project_path.exists(): # prevent overwriting
        print(f"error: {project_name} already exists at {project_path}. Exiting.")
        sys.exit(1)

    project_path.mkdir(parents=True)
    print(f"created project folder: {project_path}")

    pyproject_content = f"""[project] # create pyproject.toml (the modern standard for project metadata)
name = "{project_name}"
version = "0.1.0"
dependencies = []
"""
    (project_path / "pyproject.toml").write_text(pyproject_content)

    # create virtual environment
    print("Installing virtual environment...")
    venv.EnvBuilder(with_pip=True).create(venv_path)

    # determine python executable (cross-platform)
    # windows uses 'scripts', unix uses 'bin'
    python_exe = venv_path / ("Scripts" if sys.platform == "win32" else "bin") / "python"

    try: # upgrade pip and install dependencies replaced 'except: pass' with actual error handling
        print("Upgrading pip...")
        subprocess.run([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"], check=True)

        # check if a global requirements.txt exists to seed the new project
        seed_reqs = Path("requirements.txt")
        if seed_reqs.exists():
            print(f"Installing dependencies from {seed_reqs.absolute()}...")
            subprocess.run([str(python_exe), "-m", "pip", "install", "-r", str(seed_reqs)], check=True)
        else:
            print("No source requirements.txt found; skipping initial package install.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during installation: {e}")
        sys.exit(1)

    # finalise everythinng
    print("-" * 30)
    print(f"Project '{project_name}' initialized successfully.")
    print(f"Location: {project_path}")
    print(f"To activate: {'source venv/bin/activate' if sys.platform != 'win32' else 'venv\\Scripts\\activate'}")

if __name__ == "__main__":
    create_project()
