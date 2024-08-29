import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")
cursor = conn.cursor()

# Execute the SELECT query with LIMIT
cursor.execute("SELECT * FROM students order by id desc")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Iterate over the rows and print them
for row in rows:
    print(row)

# Close the connection
conn.close()
