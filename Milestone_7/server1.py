from flask import Flask, request, jsonify
import csv
import datetime

app = Flask(__name__)

# Load employee data from database.csv
def load_employee_data():
    with open('..\Milestone_5\database.csv', mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# Sample employee data (replace this with your actual database)
employees = load_employee_data()

@app.route('/birthdays')
def birthdays():
    month_name = request.args.get('month')
    department = request.args.get('department')

    month_number = datetime.datetime.strptime(month_name, '%b').month


    filtered_employees = [emp for emp in employees if emp['Department'] == department and datetime.date.fromisoformat(emp['Birthday']).month == month_number]
    #filtered_employees = [emp for emp in employees if emp['Department'] == department and emp['Birthday'].startswith(month_name)]

    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }
    return jsonify(response)

@app.route('/show_all')
def show_all():
    response = {
        "total": len(employees),
        "employees": employees
    }
    return jsonify(response)

@app.route('/anniversaries')
def anniversaries():
    month_number = request.args.get('month')
    department = request.args.get('department')

    # Convert month number to month name
    month_name = calendar.month_name[int(month_number)]

    filtered_employees = [emp for emp in employees if emp['Department'] == department and emp['Hiring Date'].startswith(month_name)]

    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

