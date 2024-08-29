import sqlite3
con=sqlite3.connect("C:/SQLite3/student")
cur=con.cursor()
cur.execute('select * from students')
data=cur.fetchall()
for row in data:
    print(row)
