import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")
cursor = conn.cursor()

# Execute the GROUP BY query
cursor.execute("select avg(fee) from students")

# Fetch all rows from the result set
average= cursor.fetchone()[0]

print('average fee:',average)


# Close the connection
conn.close()
