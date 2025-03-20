#!/usr/bin/env python3

import os
import sys
import subprocess

PROJECT_STRUCTURE = [
    "notebooks/",
    "src/",
    "src/__init__.py",
    "src/main.py",
    "src/utils.py",
    "tests/",
    "tests/test_main.py",
    "data/",
    "results/",
    "requirements.txt",
    ".gitignore",
    "README.md"
]

GITIGNORE_CONTENT = """\
venv/
__pycache__/
*.pyc
*.pyo
.DS_Store
*.ipynb_checkpoints
"""

README_CONTENT = """\
# {project_name}

## Installation
```bash
git clone https://github.com/jackhenry02/{project_name}.git
cd {project_name}
python -m venv venv
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
"""