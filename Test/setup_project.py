import os
import subprocess

# Step 1: Ask for the location and name of the new project
project_location = input("Enter the path where you'd like to create the project (e.g., /Users/yourname/Projects): ")
project_name = input("Enter the name of the new project: ")

# Combine path and project name to get full path
project_path = os.path.join(project_location, project_name)

# Step 2: Create project folder
os.makedirs(f"{project_path}/src", exist_ok=True)
os.makedirs(f"{project_path}/tests", exist_ok=True)

# Step 3: Create README.md
with open(f"{project_path}/README.md", "w") as f:
    f.write("# " + project_name + "\n\n")
    f.write("## Overview\n")
    f.write(f"This is the {project_name} project.\n\n")
    f.write("## Installation\n")
    f.write("To set up this project, run:\n")
    f.write("```bash\n")
    f.write(f"git clone https://github.com/jackhenry02/{project_name}.git\n")
    f.write(f"cd {project_name}\n")
    f.write("python -m venv venv\n")
    f.write("source venv/bin/activate  # For Mac/Linux\n")
    f.write("pip install -r requirements.txt\n")
    f.write("```\n")
    f.write("\n## Usage\n")
    f.write("Run the main program:\n")
    f.write("```bash\n")
    f.write("python src/main.py\n")
    f.write("```")

# Step 4: Create .gitignore
with open(f"{project_path}/.gitignore", "w") as f:
    f.write("venv/\n")
    f.write("__pycache__/\n")
    f.write("*.pyc\n")
    f.write("*.pyo\n")
    f.write(".DS_Store\n")
    f.write("*.ipynb_checkpoints\n")

# Step 5: Create requirements.txt
with open(f"{project_path}/requirements.txt", "w") as f:
    f.write("# Add your dependencies here, for example:\n")
    f.write("numpy==1.21.2\n")
    f.write("pandas==1.3.3\n")

# Step 6: Create main.py inside src
with open(f"{project_path}/src/main.py", "w") as f:
    f.write("def main():\n")
    f.write("    print('Hello, World!')\n\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    main()\n")

# Step 7: Create __init__.py inside src
with open(f"{project_path}/src/__init__.py", "w") as f:
    f.write("# This file makes the src directory a Python package.\n")
    f.write("# Leave it empty for now.\n")

# Step 8: Create utils.py inside src
with open(f"{project_path}/src/utils.py", "w") as f:
    f.write("def helper_function():\n")
    f.write("    print('This is a helper function!')\n")

# Step 9: Create test_main.py inside tests
with open(f"{project_path}/tests/test_main.py", "w") as f:
    f.write("import unittest\n")
    f.write("from src.main import main\n\n")
    f.write("class TestMain(unittest.TestCase):\n")
    f.write("    def test_main(self):\n")
    f.write("        # Simply checking if it runs without errors\n")
    f.write("        self.assertIsNone(main())\n\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    unittest.main()\n")

# Step 10: Ask for new branch name and create the branch
branch_name = input("Enter the name of the new branch (or press Enter to skip): ")

if branch_name:
    # Initialize git repository if not already initialized
    os.system(f"git init {project_path}")
    
    # Create and switch to the new branch
    subprocess.run(["git", "checkout", "-b", branch_name], cwd=project_path)
    print(f"Switched to new branch: {branch_name}")
else:
    print("No new branch created, working on the main branch.")

# Step 11: Create virtual environment
os.system(f"python3 -m venv {project_path}/venv")

# Step 12: Install dependencies
subprocess.run(["pip", "install", "-r", f"{project_path}/requirements.txt"], cwd=project_path)

# Step 13: Activate the virtual environment (Mac/Linux)
print(f"Virtual environment activated! You can now work in {project_path}.")

print("Project setup complete!")
