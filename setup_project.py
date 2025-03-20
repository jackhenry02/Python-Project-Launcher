import os
import subprocess

# Step 1: Create project folder
os.makedirs("MyNewProject/src", exist_ok=True)
os.makedirs("MyNewProject/tests", exist_ok=True)

# Step 2: Create README.md
with open("MyNewProject/README.md", "w") as f:
    f.write("# MyNewProject\n\n")
    f.write("## Overview\n")
    f.write("This is a basic template for a Python project.\n\n")
    f.write("## Installation\n")
    f.write("To set up this project, run:\n")
    f.write("```bash\n")
    f.write("git clone https://github.com/jackhenry02/MyNewProject.git\n")
    f.write("cd MyNewProject\n")
    f.write("python -m venv venv\n")
    f.write("source venv/bin/activate  # For Mac/Linux\n")
    f.write("pip install -r requirements.txt\n")
    f.write("```\n")
    f.write("\n## Usage\n")
    f.write("Run the main program:\n")
    f.write("```bash\n")
    f.write("python src/main.py\n")
    f.write("```")

# Step 3: Create .gitignore
with open("MyNewProject/.gitignore", "w") as f:
    f.write("venv/\n")
    f.write("__pycache__/\n")
    f.write("*.pyc\n")
    f.write("*.pyo\n")
    f.write(".DS_Store\n")
    f.write("*.ipynb_checkpoints\n")

# Step 4: Create requirements.txt
with open("MyNewProject/requirements.txt", "w") as f:
    f.write("# Add your dependencies here, for example:\n")
    f.write("numpy==1.21.2\n")
    f.write("pandas==1.3.3\n")

# Step 5: Create main.py inside src
with open("MyNewProject/src/main.py", "w") as f:
    f.write("def main():\n")
    f.write("    print('Hello, World!')\n\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    main()\n")

# Step 6: Create __init__.py inside src
with open("MyNewProject/src/__init__.py", "w") as f:
    f.write("# This file makes the src directory a Python package.\n")
    f.write("# Leave it empty for now.\n")

# Step 7: Create utils.py inside src
with open("MyNewProject/src/utils.py", "w") as f:
    f.write("def helper_function():\n")
    f.write("    print('This is a helper function!')\n")

# Step 8: Create test_main.py inside tests
with open("MyNewProject/tests/test_main.py", "w") as f:
    f.write("import unittest\n")
    f.write("from src.main import main\n\n")
    f.write("class TestMain(unittest.TestCase):\n")
    f.write("    def test_main(self):\n")
    f.write("        # Simply checking if it runs without errors\n")
    f.write("        self.assertIsNone(main())\n\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    unittest.main()\n")

# Step 9: Create virtual environment
os.system("python3 -m venv MyNewProject/venv")

# Step 10: Ask for new branch name and create the branch
branch_name = input("Enter the name of the new branch (or press Enter to skip): ")

if branch_name:
    # Initialize git repository if not already initialized
    os.system("git init MyNewProject")
    
    # Create and switch to the new branch
    subprocess.run(["git", "checkout", "-b", branch_name], cwd="MyNewProject")
    print(f"Switched to new branch: {branch_name}")
else:
    print("No new branch created, working on the main branch.")

# Step 11: Create the folder structure
os.makedirs("MyNewProject/venv", exist_ok=True)

print("Project structure has been set up!")

