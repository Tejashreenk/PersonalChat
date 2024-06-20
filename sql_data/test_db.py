import sqlite3
import os

directory = './'
database_file = 'MyCompany.db'
database_path = os.path.join(directory, database_file)

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('MyCompany.db')

# Create a cursor object
cursor = conn.cursor()

# Function to print the schema of the database using sqlite_master
def print_db_schema(cursor):
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        print(table[0])

# Print the schema of the database
print("Database schema:")
print_db_schema(cursor)

# Close the connection
conn.close()
# rows = cursor.fetchall()
# print(rows)

def print_query_results(rows):
    for row in rows:
        print(f"{row}")
