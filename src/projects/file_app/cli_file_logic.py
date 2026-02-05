from pathlib import Path

def process_file(input_path, output_path, uppercase=False):
    input_file = Path(input_path)
    output_file = Path(output_path)

    content = input_file.read_text(encoding="utf-8").splitlines()

    if uppercase:
        content = [line.upper() for line in content]

    output_file.write_text("\n".join(content), encoding="utf-8")

    print("Processing complete.")
