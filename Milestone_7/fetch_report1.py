import requests
import sys

def fetch_report(month, department):
    url = f"http://localhost:5000/birthdays?month={month}&department={department}"
    response = requests.get(url)
    if response.status_code == 200:
        report = response.json()
        print(f"Report for {department} department for {month} fetched.")
        print(f"Total: {report['total']}")
    
        print("Employees:")
        for employee in report['employees']:
            # Adjusted to match the new format of the employee data
            name = employee['Name']
            birthday = employee['Birthday']
            print(f"- {birthday}, {name}")
    else:
        print("Failed to fetch report.")
        print(f"Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fetch_report.py <month> <department>")
        sys.exit(1)

    month = sys.argv[1]
    department = sys.argv[2]
    fetch_report(month, department)
