from pathlib import Path
import shutil

archive = Path("archive")
files = Path("files")
archive.mkdir(exist_ok=True)

source = Path("files/hello.txt")
destination = archive / "hello_backup.txt"

shutil.move(source, destination)
shutil.copy(destination, files / "hello_copy.txt")

for a in archive.iterdir():
    print(a)
    print(a.resolve())

for f in files.iterdir():
    print(f) 
    print(f.resolve())