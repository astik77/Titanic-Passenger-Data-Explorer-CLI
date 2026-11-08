import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent              

DATA_PATH = PROJECT_ROOT / "data" / "raw" / "train.csv"

# Minimum required columns in the Titanic dataset
REQUIRED_COLUMNS = {"PassengerId", "Survived", "Pclass"}

"""
__file__    ----> refers to the current Python file (main.py).



.resolve()  ----> obtains its absolute path.



.parent     ----> obtains the directory containing main.py.



/           ----> joins path components using pathlib
"""

# define the following missing-value policy
MISSING_MARKERS = {"", "na", "n/a", "null"}
def is_missing(value):
    if value is None:
        return True

    return str(value).strip().lower() in MISSING_MARKERS
            
# Calculate missing values for each column
def analyze_missing_values(rows, headers):
    missing_counts = {}
    for column in headers:
        count = 0
        for row in rows:
            if is_missing(row.get(column)):
                count += 1
                    
        missing_counts[column] = count
    return missing_counts

def inspect_csv(file_path):

    file_path = Path(file_path)

    # Check whether the file exists
    if not file_path.exists():
        print("Error: Dataset file does not exist.")
        return

    # Check whether the path represents a file
    if not file_path.is_file():
        print("Error: The provided path is not a file.")
        return

    try:

        with file_path.open(
            mode="r",
            encoding="utf-8-sig",
            newline=""
        ) as file:

            # CSV processing will happen here
            reader = csv.DictReader(file, strict=True)      # CSV reader
            
            headers = reader.fieldnames

            if not headers:
                print("Error: CSV is empty or missing its header row.")
                return

            # Remove unnecessary whitespace from column names
            headers = [header.strip() for header in headers]

            # Check for empty column names
            if any(not header for header in headers):
                print("Error: CSV contains an empty column name.")
                return

            # Check for duplicate column names
            if len(headers) != len(set(headers)):
                print("Error: CSV contains duplicate column names.")
                return

            # Update DictReader with normalized headers
            reader.fieldnames = headers
            
            missing_columns = REQUIRED_COLUMNS - set(headers)

            if missing_columns:
                print(
                    "Error: Unexpected CSV structure. "
                    f"Missing columns: {sorted(missing_columns)}"
                )
                return
            
            rows = list(reader)
            if not rows:
                print("\nNo passenger records found.")
            
            print("\n[1] Dataset Information")
            print(f"Dataset: {file_path.name}")
            print(f"Columns: {len(headers)}")
            print(f"Total Records: {len(rows)}")

            print("\n[2] Column Names")

            for header in headers:
                print(header)

            print("\n[3] First 5 Records")

            for index, row in enumerate(rows[:5], start=1):
                print(f"Record {index}: {row}")
                
            malformed_records = []

            for index, row in enumerate(rows, start=1):

                has_extra_fields = None in row

                has_missing_fields = any(
                    row[column] is None
                    for column in headers
                )

                if has_extra_fields or has_missing_fields:
                    malformed_records.append(index)

            if malformed_records:
                print(
                    "\nWarning: Unexpected row structures found in records:",
                    malformed_records
                )
            else:
                print("\nAll records have a consistent structure.")
            
    except OSError as error:
        print(f"File error: {error}")

    except UnicodeDecodeError as error:
        print(f"Encoding error: {error}")

    except csv.Error as error:
        print(f"CSV parsing error: {error}")

def main():
    print("=================================")
    print("     TITANIC DATA EXPLORER")
    print("=================================")

    inspect_csv(DATA_PATH)


if __name__ == "__main__":
    main()