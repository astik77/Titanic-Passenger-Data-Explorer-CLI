import csv
from pathlib import Path
from collections import Counter

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

def calculate_missing_percentage(missing_count, total_records):

    if total_records == 0:
        return 0

    percentage = (missing_count / total_records) * 100

    return round(percentage, 2)

def display_missing_report(rows, headers):

    missing_counts = analyze_missing_values(rows, headers)

    total_records = len(rows)

    print("\n========================================")
    print("          MISSING VALUE REPORT")
    print("========================================")

    print(f"{'Column':<20} {'Missing':<12} {'Percentage'}")
    print("-" * 50)

    for column, count in missing_counts.items():

        percentage = calculate_missing_percentage(
            count,
            total_records
        )

        print(f"{column:<20} {count:<12} {percentage}%")

def analyze_categorical_column(rows, column):
    values = []

    for row in rows:
        value = row.get(column)

        if not is_missing(value):
            values.append(value)

    frequency = Counter(values)
    
    return frequency

def analyze_unique_values(rows, column):
    values = []

    for row in rows:
        value = row.get(column)
        if not is_missing(value):
            values.append(value)
    
    unique_values = set(values)
    sorted_values = sorted(unique_values)
    
    return sorted_values

def find_duplicate_rows(rows, headers):
    row_signatures = []

    for row in rows:
        row_signature = tuple(row.get(column) for column in headers)
        row_signatures.append(row_signature)

    row_counts = Counter(row_signatures)

    duplicates = {
        row: count
        for row, count in row_counts.items()
        if count > 1
    }

    return duplicates


def find_duplicate_passenger_ids(rows):
    passenger_ids = []

    for row in rows:
        passenger_id = row.get("PassengerId")

        if not is_missing(passenger_id):
            passenger_ids.append(passenger_id)

    id_counts = Counter(passenger_ids)

    duplicates = {
        passenger_id: count
        for passenger_id, count in id_counts.items()
        if count > 1
    }

    return duplicates

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

            display_missing_report(rows, headers)
            
            # Categorical Frequency Analysis
            print("\n========================================")
            print("       CATEGORICAL FREQUENCY REPORT")
            print("========================================")

            categorical_columns = ["Sex", "Pclass", "Embarked"]

            for column in categorical_columns:
                frequency = analyze_categorical_column(rows, column)

                print(f"\n{column}:")

                for value, count in frequency.items():
                    print(f"  {value}: {count}")
                    
            # Unique Value Analysis
            print("\n========================================")
            print("       UNIQUE VALUE REPORT")
            print("========================================")

            categorical_columns = ["Sex", "Pclass", "Embarked", "Survived"]
            
            for column in categorical_columns:
                print(f"{column}- ")
                print(analyze_unique_values(rows, column))
                
            # Duplicate Detection
            print("\n========================================")
            print("          DUPLICATE DETECTION")
            print("========================================")

            duplicate_rows = find_duplicate_rows(rows, headers)

            print("\nExact Duplicate Rows:")

            if duplicate_rows:
                for row, count in duplicate_rows.items():
                    print(f"Record: {row}")
                    print(f"Occurrences: {count}")
            else:
                print("No exact duplicate rows found.")

            duplicate_ids = find_duplicate_passenger_ids(rows)

            print("\nDuplicate Passenger IDs:")

            if duplicate_ids:
                for passenger_id, count in duplicate_ids.items():
                    print(f"Passenger ID: {passenger_id} | Occurrences: {count}")
            else:
                print("No duplicate Passenger IDs found.")
            
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