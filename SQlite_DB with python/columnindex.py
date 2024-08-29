import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")
cursor = conn.cursor()

# Execute the CREATE INDEX statement
cursor.execute("CREATE INDEX id_index ON students (id)")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
