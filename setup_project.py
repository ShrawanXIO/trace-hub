import os

# Updated folder structure including TDD directories
folders = [
    "app/core",
    "app/db",
    "app/settings",
    "app/ui",
    "database",
    "engine",
    "data/outputs",
    "tests/unit",          # For individual agent tests
    "tests/integration",   # For end-to-end engine flow tests
    "tests/fixtures"       # For sample user stories/docs
]

# Updated file list including test configs and README
files = {
    "app/__init__.py": "",
    "app/core/__init__.py": "",
    "app/db/__init__.py": "",
    "app/settings/__init__.py": "",
    "app/ui/__init__.py": "",
    "engine/__init__.py": "",
    "main.py": "",
    ".env": "OPENAI_API_KEY=\nOLLAMA_BASE_URL=http://localhost:11434\nDATABASE_URL=sqlite:///./database/trace_hub.db",
    ".gitignore": ".venv/\n__pycache__/\n.env\ndatabase/*.db\ndata/outputs/*.csv",
    "requirements.txt": "chainlit\nlangchain-ollama\nlangchain-openai\nlangchain-core\nsqlalchemy\npython-dotenv\npandas\npytest\npytest-asyncio",
    "README.md": "# Trace Hub\n\nExtension for Trace Auto-Gen engine. Multi-agent RAG system for high-quality test generation.",
    "pytest.ini": "[pytest]\nasyncio_mode = auto\ntestpaths = tests",
    "tests/__init__.py": "",
    "tests/unit/__init__.py": "",
    "tests/integration/__init__.py": "",
    "tests/conftest.py": ""
}

def create_boilerplate():
    print("--- Updating Trace Hub Structure for TDD ---")
    
    # Create directories
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")

    # Create files with initial content
    for file_path, content in files.items():
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created file: {file_path}")

    print("\nProject structure and Test folders are ready.")

if __name__ == "__main__":
    create_boilerplate()