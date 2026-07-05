from pathlib import Path

def count_lines(project_path):
    path = Path(project_path)

    total_lines = 0

    for file in path.rglob("*.py"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                total_lines += len(f.readlines())
        except Exception:
            pass

    return total_lines
import ast

def count_functions(project_path):
    path = Path(project_path)

    total_functions = 0

    for file in path.rglob("*.py"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    total_functions += 1
        except Exception:
            pass

    return total_functions
import ast

def count_functions(project_path):
    path = Path(project_path)

    total_functions = 0

    for file in path.rglob("*.py"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    total_functions += 1
        except Exception:
            pass

    return total_functions
def count_classes(project_path):
    path = Path(project_path)

    total_classes = 0

    for file in path.rglob("*.py"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    total_classes += 1
        except Exception:
            pass

    return total_classes
def list_imports(project_path):
    path = Path(project_path)

    imports = set()

    for file in path.rglob("*.py"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.add(alias.name)

                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.add(node.module)

        except Exception:
            pass

    return sorted(imports)
def find_todos(project_path):
    path = Path(project_path)

    todos = []

    for file in path.rglob("*.py"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line_no, line in enumerate(f, start=1):
                    if "TODO" in line or "FIXME" in line:
                        todos.append(f"{file.relative_to(path)} : Line {line_no} -> {line.strip()}")
        except Exception:
            pass

    return todos
import re

def detect_secrets(project_path):
    path = Path(project_path)

    patterns = [
        r"API_KEY\s*=",
        r"SECRET_KEY\s*=",
        r"PASSWORD\s*=",
        r"TOKEN\s*=",
    ]

    secrets = []

    for file in path.rglob("*.py"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line_no, line in enumerate(f, start=1):
                    for pattern in patterns:
                        if re.search(pattern, line):
                            secrets.append(
                                f"{file.relative_to(path)} : Line {line_no} -> {line.strip()}"
                            )
        except Exception:
            pass

    return secrets