import os

# -------- CONFIG ---------

# Root = current directory
ROOT = os.getcwd()

# Folder structure definition
structure = {
    "data": [
        "equity_holdings.csv",
        "fixed_income_holdings.csv",
        "benchmark.csv",
        "prices.csv",
        "rates.csv"
    ],
    "modules": [
        "ingestion_engine.py",
        "returns_engine.py",
        "attribution_engine.py",
        "residual_analyzer.py",
        "reporting_engine.py",
        "__init__.py"
    ],
    "dashboard": [
        "app.py"
    ],
    "airflow/dags": [
        "mappa_daily_workflow.py"
    ],
    "notebooks": [
        "attribution_demo.ipynb"
    ],
    "scripts": [
        "generate_synthetic_data.py"
    ],
    "docs": [
        "system_design.md"
    ]
}

root_files = [
    "README.md",
    "requirements.txt",
    ".gitignore"
]

# -------- CREATE STRUCTURE ---------

def create_file(path):
    """Create an empty file if it doesn't exist."""
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("")   # empty placeholder
        print(f"Created file: {path}")
    else:
        print(f"Skipped (exists): {path}")

def create_folder(path):
    """Create folder if not exists."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print(f"Folder exists: {path}")

def main():
    # Create top-level files
    for file in root_files:
        create_file(os.path.join(ROOT, file))

    # Create subfolders + files
    for folder, files in structure.items():
        folder_path = os.path.join(ROOT, folder)
        create_folder(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)
            create_file(file_path)

    print("\n✔ Project structure created successfully!")

if __name__ == "__main__":
    main()
