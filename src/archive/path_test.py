from pathlib import Path

current_dir = Path(".")
files_folder = Path("files")
full_path = files_folder / "hello.txt"

lines = full_path.read_text(encoding="utf-8").splitlines()
for line in lines:
    print(line)

with full_path.open("a", encoding="utf-8") as f:
    f.write("\nPathlib is clean")

updated_lines = full_path.read_text(encoding="utf-8").splitlines()
for line in updated_lines:
    print(line)

print(full_path.exists())
print(full_path)