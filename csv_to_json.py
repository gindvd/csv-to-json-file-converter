import json
import csv
import sys
import os


def csv_to_json(csv_file: str, json_file: str) -> None:
    """ Reads data inside CSV file, converts to a Python dictionary and dumps into a JSON file """
    
    with open(csv_file, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Removes key if value doesn't exist
        data = [
            {key: value for key, value in row.items() if value}
            for row in reader
        ]

    with open(json_file, mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)


def check_files(csv_file: str, json_file: str) -> None:
    
    if not os.path.isfile(csv_file):
        print("CSV file does not exist!")
        print("Usage: python csv_to_json.py <path/to/file/file.csv> <path/to/file/file.json>")
        sys.exit(1)
    
    _, ext = os.path.splittext(csv_file)

    if ext != "csv":
        print("No valid CSV file found!")
        print("Usage: python csv_to_json.py <path/to/file/file.csv> <path/to/file/file.json>")
        sys.exit(1)
    
    _, ext = os.path.splittext(json_file)

    if ext != "json":
        print("No valid JSON file found!")
        print("Usage: python csv_to_json.py <path/to/file/file.csv> <path/to/file/file.json>")
        sys.exit(1)


def main() -> None:
    if len(sys.argv) == 3:
        csv_file = sys.argv[1]
        json_file = sys.argv[2]
    
    elif len(sys.argv) == 2:
        csv_file = sys.argv[1]

        print("No output JSON file specified!\n")
        print("Do you wish to save to output.json? Y/N: ")

        response = input().strip()
        
        # Allows JSON to be written to default if no JSON file is given as arg
        if response.lower() in ("y", "yes"):
            json_file = "output.json"
        
        else:
            print("Need path to JSON file!")
            print("Usage: python csv_to_json.py <path/to/file/file.csv> <path/to/file/file.json>")
            sys.exit(1)
    
    else:
        print("Need path to input and output files!")
        print("Usage: python csv_to_json.py <path/to/file/file.csv> <path/to/file/file.json>")
        sys.exit(1)

    check_files(csv_file, json_file)
    
    csv_to_json(csv_file, json_file)

    print(f"CSV file contents written to {json_file}")


if __name__ == "__main__":
    main()
