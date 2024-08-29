import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")
cursor = conn.cursor()

# Execute PRAGMA statement to get table information
cursor.execute("PRAGMA table_info(students)")

# Fetch all rows from the result set
columns = cursor.fetchall()

# Extract column names from the result set
column_names = [column[1] for column in columns]

# Print the column names
print("Column names:", column_names)

# Close the connection
conn.close()
