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