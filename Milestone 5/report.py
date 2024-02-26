

import argparse
import csv
from datetime import datetime

def generate_report(csv_file, month, verbose=False):
    # Open the CSV file and read its contents
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Convert 'Birthday' column to datetime type and filter data for the specified month
    month_data = []
    for row in data:
        birthday = datetime.strptime(row['Birthday'], '%Y-%m-%d')
        if birthday.strftime('%B').lower() == month.lower():
            row['Birthday'] = birthday
            row['Hiring Date'] = datetime.strptime(row['Hiring Date'], '%Y-%m-%d')
            month_data.append(row)

    # Count birthdays and anniversaries by department
    birthdays_by_dept = {}
    anniversaries_by_dept = {}
    for row in month_data:
        if row['Birthday'].day > 0:
            birthdays_by_dept[row['Department']] = birthdays_by_dept.get(row['Department'], 0) + 1
        if row['Hiring Date'].day > 0:
            anniversaries_by_dept[row['Department']] = anniversaries_by_dept.get(row['Department'], 0) + 1

    # Print report
    print(f"Report for {month.capitalize()} generated")
    print("--- Birthdays ---")
    print(f"Total: {sum(1 for row in month_data if row['Birthday'].day > 0)}")
    print("By department:")
    for dept, count in birthdays_by_dept.items():
        print(f"- {dept}: {count}")
    print("--- Anniversaries ---")
    print(f"Total: {sum(1 for row in month_data if row['Hiring Date'].day > 0)}")
    print("By department:")
    for dept, count in anniversaries_by_dept.items():
        print(f"- {dept}: {count}")

    # Verbose mode: Print employee names
    if verbose:
        print("--- Employee Names ---")
        for row in month_data:
            print(f"{row['Name']}: {row['Department']}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate monthly report")
    parser.add_argument("csv_file", type=str, help="Path to CSV file")
    parser.add_argument("month", type=str, help="Month (e.g., January, February, etc.)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print employee names")
    args = parser.parse_args()

    # Generate report
    generate_report(args.csv_file, args.month, args.verbose)

