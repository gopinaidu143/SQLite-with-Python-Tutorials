import sqlite3
con=sqlite3.connect("C:/SQLite3/student")
cur=con.cursor()
cur.execute("select count(*) from students")
rows=cur.fetchone()[0]
print('total no. of rows:',rows)
con.close()

