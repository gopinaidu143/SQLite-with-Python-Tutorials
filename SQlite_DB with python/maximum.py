import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")
cursor = conn.cursor()

# Execute the GROUP BY query
cursor.execute("select max(fee) from students")

# Fetch all rows from the result set
maximum= cursor.fetchone()[0]

print('maximum fee:',maximum)


# Close the connection
conn.close()
