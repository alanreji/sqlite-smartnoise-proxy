import csv
import sqlite3
import os

# Check if the database file exists
if not os.path.exists('data/db/employees.db'):
    # Create a connection to the database
    # If it doesn't exist, create it
    conn = sqlite3.connect('data/db/employees.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table for the employees
    cursor.execute('''CREATE TABLE employees
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT, salary REAL, phone TEXT)''')

    # Read the employee data from the CSV file
    with open('data/employees.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            cursor.execute("INSERT INTO employees (id, name, email, salary, phone) VALUES (?, ?, ?, ?, ?)", 
                    (row[0], row[1], row[2], row[3], row[4]))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()
