import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")
cursor = conn.cursor()

# Execute the wildcard search query
search_term = "an"
cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + search_term + '%',))

# Fetch all rows from the result set
rows = cursor.fetchall()

# Iterate over the rows and print them
for row in rows:
    print(row)

# Close the connection
conn.close()
