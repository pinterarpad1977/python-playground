from pathlib import Path

def process_file():
    BASE_DIR = Path(__file__).parent #the folder contains this partcular file
    data_folder = BASE_DIR / "data"
    input_file = data_folder / "input.txt"
    output_file = data_folder / "output.txt"

    # Read input
    content = input_file.read_text(encoding="utf-8").splitlines()

    # Transform (placeholder logic)
    transformed = [line.upper() for line in content]

    # Write output
    output_file.write_text("\n".join(transformed), encoding="utf-8")

    print("Processing complete.")
