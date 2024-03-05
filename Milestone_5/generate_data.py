import csv
from faker import Faker
from datetime import datetime

# Create a Faker instance
fake = Faker()

# Define the number of employees
num_employees = 100

# Define the header for the CSV file
header = ['Name', 'Hiring Date', 'Department', 'Birthday']

# Open the CSV file in write mode
with open('database.csv', mode='w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the header to the CSV file
    writer.writerow(header)

    # Generate and write data for each employee
    for _ in range(num_employees):
        # Generate employee data
        name = fake.name()
        hiring_date = fake.date_between(start_date='-5y', end_date='today')
        department = fake.random_element(elements=('Engineering', 'Marketing', 'Sales', 'HR'))
        birthday = fake.date_of_birth(minimum_age=22, maximum_age=65)

        # Format dates as strings
        hiring_date_str = hiring_date.strftime('%Y-%m-%d')
        birthday_str = birthday.strftime('%Y-%m-%d')

        # Write employee data to the CSV file
        writer.writerow([name, hiring_date_str, department, birthday_str])

print("Data has been written to database.csv")
 
