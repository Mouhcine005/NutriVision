
from pathlib import Path

# Root directory = location of this script
ROOT = Path(__file__).resolve().parent

# Project directories
directories = [
    "data/raw",
    "data/interim",
    "data/processed",
    "notebooks",
    "src/data",
    "src/features",
    "src/utils",
    "reports/figures",
    "tests",
]

# Create directories
for directory in directories:
    (ROOT / directory).mkdir(parents=True, exist_ok=True)

# Initial files and their contents
files = {
    "README.md": """# NutriVision

A Multimodal AI System for Food Recognition,
Ingredient Extraction, and Nutritional Estimation.

## Project Overview

NutriVision combines Computer Vision and NLP
to recognize food, extract ingredients, and estimate
nutritional information from food images and text.

## Project Structure

- data/: Dataset storage
- notebooks/: Data exploration and experimentation
- src/: Reusable Python modules
- reports/: Analysis results and visualizations
- tests/: Unit tests

## Technologies

Python, Pandas, NumPy, Scikit-learn,
PyTorch, Computer Vision, NLP.
""",

    "data/README.md": """# Data Directory

- raw/: Original datasets (never modify)
- interim/: Intermediate processing outputs
- processed/: Clean datasets ready for modeling

Dataset files are excluded from Git.
""",

    "requirements.txt": """pandas
numpy
matplotlib
seaborn
jupyter
Pillow
tqdm
scikit-learn
""",

    ".gitignore": """# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
.env

# Jupyter
.ipynb_checkpoints/

# Data
data/raw/*
data/interim/*
data/processed/*
!data/raw/.gitkeep
!data/interim/.gitkeep
!data/processed/.gitkeep

# Generated outputs
reports/figures/*
!reports/figures/.gitkeep

# IDE
.vscode/
.idea/
"""
}

# Create files without overwriting existing ones
for filename, content in files.items():
    path = ROOT / filename
    if not path.exists():
        path.write_text(content, encoding="utf-8")

# Keep empty directories in Git
for directory in [
    "data/raw",
    "data/interim",
    "data/processed",
    "reports/figures",
]:
    (ROOT / directory / ".gitkeep").touch(exist_ok=True)

print("NutriVision project initialized successfully!")