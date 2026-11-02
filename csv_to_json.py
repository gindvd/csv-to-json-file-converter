import json
import csv
import sys

from pathlib import Path


def csv_to_json(csv_file: str, json_file: str) -> None:
    """ Reads data inside CSV file, converts to a Python dictionary and dumps into a JSON file """
    
    with open(csv_file, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Removes empty values
        data = [
            {key: value for key, value in row.items() if value}
            for row in reader
        ]

    with open(json_file, mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)


def check_files(csv_file: str, json_file: str) -> None:
    csv_path = Path(csv_file)
    json_path = Path(json_file)
    
    if csv_path.suffix != ".csv":
        exit_with_message(f"{csv_file} not a vlid CSV file!")

    if not csv_file.is_file():
        exit_with_message(f"{csv_file} file not found!")

    if json_path.suffix != ".json":
        exit_with_message(f"{json_file} not a valid JSON file")


def ask_for_default_file() -> str:
    print("No output JSON file specified!\n")
    print("Do you wish to save to output.json? Y/N: ")

    response = input().strip()
    
    # Allows JSON to be written to default if no JSON file is given as arg
    if response.lower() in ("y", "yes"):
        return "output.json"
    
    exit_with_message("Need path to JSON file!")


def exit_with_message(msg: str) -> None:
    print(msg)
    print("Usage: python csv_to_json.py <path/to/file.csv> <path/to/file.json>")

    sys.exit(1)


def main() -> None:

    if len(sys.argv) == 3:
        csv_file = sys.argv[1]
        json_file = sys.argv[2]
    
    elif len(sys.argv) == 2:
        csv_file = sys.argv[1]

        json_file = ask_for_default_file()
    
    else:
        exit_with_message("Need path to input and output files!")

    check_files(csv_file, json_file)
    csv_to_json(csv_file, json_file)

    print(f"CSV file contents written to {json_file}")
    

if __name__ == "__main__":
    main()
