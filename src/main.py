from scanner import scan_project
from analyzer import count_lines, count_functions
from analyzer import count_lines


print("🚀 CodeVision AI")
print("-" * 30)

project_path = input("Enter project path: ")

scan_project(project_path)

print(f"\nTotal Lines of Code : {count_lines(project_path)}")
print(f"Total Functions : {count_functions(project_path)}")