from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample employee data (replace this with your actual database)
employees = [
    {"id": 1, "name": "John Doe", "birthday": "Apr 18", "department": "HR"},
    {"id": 2, "name": "Jane Smith", "birthday": "May 12", "department": "IT"},
    {"id": 3, "name": "Alice Johnson", "birthday": "Apr 5", "department": "HR"}
]

@app.route('/birthdays')
def birthdays():
    month = request.args.get('month')
    department = request.args.get('department')

    filtered_employees = [emp for emp in employees if emp['department'] == department and emp['birthday'].startswith(month.capitalize())]
    
    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }
    return jsonify(response)

@app.route('/anniversaries')
def anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')

    filtered_employees = [emp for emp in employees if emp['department'] == department and emp['hire_date'].startswith(month.capitalize())]
    
    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


   

