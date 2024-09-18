# 


import sqlite3
import pandas as pd

# Uncomment and adjust this line if you need to load a CSV file into a DataFrame
# df = pd.read_csv('Book2.csv')

# Connect to SQLite database (this will create the file if it doesn't exist)
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Create the table (corrected syntax)
create_table_query = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""
cursor.execute(create_table_query)

# Insert some records into the table
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Harsh', 'Data sci', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('ram', 'Data sci', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('mohan', 'Devops', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('sam', 'Devops', 'A', 35)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('jack', 'Data sci', 'A', 86)''')

# Commit the changes to the database
connection.commit()

# Display all the records
print("The inserted records are:")

# Query the database
data = cursor.execute('''SELECT * FROM STUDENT''')

# Print the results
for row in data:
    print(row)

# Close the connection
connection.close()
