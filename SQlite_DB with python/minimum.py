import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")
cursor = conn.cursor()

# Execute the GROUP BY query
cursor.execute("select min(fee) from students")

# Fetch all rows from the result set
minimum= cursor.fetchone()[0]

print('maximum fee:',minimum)


# Close the connection
conn.close()
