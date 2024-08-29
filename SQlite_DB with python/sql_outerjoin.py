import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")
cursor = conn.cursor()

# Execute the OUTER JOIN query
cursor.execute("""
   SELECT * FROM students AS students left JOIN exams AS exams ON students.id = exams.stu_id
    UNION
   SELECT * FROM students AS students right JOIN exams AS exams ON students.id = exams.stu_id
    WHERE students.id IS NULL
""")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Iterate over the rows and print them
for row in rows:
    print(row)

# Close the connection
conn.close()
