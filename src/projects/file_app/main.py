import argparse
from cli_file_logic import process_file

def main():
    parser = argparse.ArgumentParser(description="File processing tool.")

    parser.add_argument("--input", required=True, help="Path to input file")
    parser.add_argument("--output", required=True, help="Path to output file")
    parser.add_argument("--uppercase", action="store_true", help="Uppercase file content")
    
    args = parser.parse_args()

    process_file(
        input_path = args.input,
        output_path = args.output,
        uppercase = args.uppercase
    )

if __name__ == "__main__":
    main()

# call this with this input in the terminal:
'''
root@8993a3f37942:/app/src/projects/file_app# 
    python main.py 
        --input data/input.txt 
        --output data/output.txt 
        --uppercase'''
