import sqlite3
import os

# Specify the directory and file name for the SQLite database
directory = './'
database_file = 'MyCompany.db'
database_path = os.path.join(directory, database_file)

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('MyCompany.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
# cursor.execute("""
# CREATE TABLE users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL
# );
# """)
cursor.execute("""
CREATE TABLE Companies (
    CompanyID INTEGER PRIMARY KEY AUTOINCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(10),
    Country VARCHAR(100),
    PhoneNumber VARCHAR(20)
);""")

cursor.execute("""CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20),
    HireDate DATE NOT NULL,
    CompanyID INT,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
);""")

cursor.execute("""CREATE TABLE Roles (
    RoleID INTEGER PRIMARY KEY AUTOINCREMENT,
    RoleName VARCHAR(100) NOT NULL,
    Description TEXT
);""")

cursor.execute("""CREATE TABLE EmployeeRoles (
    EmployeeRoleID INTEGER PRIMARY KEY AUTOINCREMENT, 
    EmployeeID INT,
    RoleID INT,
    AssignedDate DATE NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);
""")

# Insert data into the table
cursor.execute('''
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')
''')
cursor.execute('''
INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')
''')

# Commit the transaction
conn.commit()

# Query the data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
conn.close()
