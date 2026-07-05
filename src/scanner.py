from pathlib import Path

def scan_project(project_path):
    path = Path(project_path)

    total_files = 0
    python_files = 0
    total_folders = 0

    # Scan project
    for item in path.rglob("*"):
        if item.is_file():
            total_files += 1
            if item.suffix == ".py":
                python_files += 1
        elif item.is_dir():
            total_folders += 1

    print(f"Project : {path.resolve().name}")
    print(f"Path    : {path.resolve()}")
    print(f"Folders : {total_folders}")
    print(f"Files   : {total_files}")
    print(f"Python Files : {python_files}")

    print("\nPython Files Found:")
    print("-" * 30)

    for item in path.rglob("*.py"):
        print(item)

    print("\nRelative Python Files:")
    print("-" * 30)

    for file in path.rglob("*.py"):
        print(file.relative_to(path))

# TODO: Add file size analysis