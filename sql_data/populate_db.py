import sqlite3
import random
import string
from faker import Faker

# Initialize Faker
fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('MyCompany.db')
cursor = conn.cursor()

# Function to generate a random phone number
def random_phone_number():
    return ''.join(random.choices(string.digits, k=10))

# Insert random data into Companies
for i in range(100):
    company_name = fake.company()
    address = fake.street_address()
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()
    country = fake.country()
    phone_number = random_phone_number()
    # company_id = i
    
    cursor.execute("""
        INSERT INTO Companies (CompanyName, Address, City, State, ZipCode, Country, PhoneNumber)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (company_name, address, city, state, zipcode, country, phone_number))

# Insert random data into Employees
for i in range(500):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone_number = random_phone_number()
    hire_date = fake.date_between(start_date='-10y', end_date='today')
    company_id = random.randint(1, 100)
    
    cursor.execute("""
        INSERT INTO Employees (FirstName, LastName, Email, PhoneNumber, HireDate, CompanyID)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (first_name, last_name, email, phone_number, hire_date, company_id))

# Insert random data into Roles
roles = ['Software Engineer', 'Project Manager', 'QA Tester', 'HR Manager', 'Accountant']
descriptions = ['Develops software solutions.', 'Manages projects.', 'Tests software for quality assurance.', 'Manages human resources.', 'Handles company finances.']

for i in range(100):
    role_name = random.choice(roles)
    description = random.choice(descriptions)
    
    cursor.execute("""
        INSERT INTO Roles (RoleName, Description)
        VALUES (?, ?)
    """, (role_name, description))

# Insert random data into EmployeeRoles
for _ in range(100):
    employee_id = random.randint(1, 100)
    role_id = random.randint(1, 100)
    assigned_date = fake.date_between(start_date='-5y', end_date='today')
    
    cursor.execute("""
        INSERT INTO EmployeeRoles (EmployeeID, RoleID, AssignedDate)
        VALUES (?, ?, ?)
    """, (employee_id, role_id, assigned_date))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("100 random records have been added to each table.")
