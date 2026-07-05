from scanner import scan_project
from analyzer import count_lines, count_functions, count_classes
from analyzer import count_lines, count_functions, count_classes, list_imports
from analyzer import (
    count_lines,
    count_functions,
    count_classes,
    list_imports,
    find_todos
)
from analyzer import (
    count_lines,
    count_functions,
    count_classes,
    list_imports,
    find_todos,
    detect_secrets
)
from report import generate_report
print("🚀 CodeVision AI")
print("-" * 30)

project_path = input("Enter project path: ")

project = scan_project(project_path)

print(f"\nTotal Lines of Code : {count_lines(project_path)}")
print(f"Total Functions : {count_functions(project_path)}")
print(f"Total Classes : {count_classes(project_path)}")
print("\nImports Used")
print("-" * 30)

for module in list_imports(project_path):
    print(module)
    print("\nTODO / FIXME")
print("-" * 30)

todos = find_todos(project_path)

if todos:
    for todo in todos:
        print(todo)
else:
    print("No TODO or FIXME found.")
    print("\nPossible Secrets")
print("-" * 30)

secrets = detect_secrets(project_path)

if secrets:
    for secret in secrets:
        print(secret)
else:
    print("No secrets found.")
    generate_report({
    "project": project["project"],
    "files": project["files"],
    "python": project["python"],
    "lines": count_lines(project_path),
    "functions": count_functions(project_path),
    "classes": count_classes(project_path)
})
    