import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")
cursor = conn.cursor()

# Execute the SELECT query with LIMIT
cursor.execute("SELECT * FROM students LIMIT 4")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Iterate over the rows and print them
for row in rows:
    print(row)

# Close the connection
conn.close()
