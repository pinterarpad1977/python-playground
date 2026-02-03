import sys

if len(sys.argv) < 2:
    print("Usage: python readfile.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    print(f.read())
