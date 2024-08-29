import sqlite3

# Connect to the database
conn = sqlite3.connect("C:/SQLite3/student")

# Create a cursor object
cursor = conn.cursor()
flag=True
while flag:
    id=int(input('enter student id:'))
    name=input('enter student name:')
    branch=input('enter student branch:')
    fee=input('enter student fee:')
    data=(id,name,branch,fee)
    cursor.execute("insert into students values(?,?,?,?)",data)
    res=input('do you want to continue(yes/no):')
    if res=='no':
        break
# Commit the changes
conn.commit()

# Close the connection
conn.close()
