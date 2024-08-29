import sqlite3
con=sqlite3.connect("C:/SQLite3/student")
cur=con.cursor()
cur.execute('BEGIN TRANSACTION')
try:
    cur.execute("insert into students values(8,'sunil','chem',25000)")
    cur.execute("update students set name='ali' where id=8")
    cur.execute("delete from students where id=6")
    con.commit()
    print('transaction successfully completed!!')

except Exception as e:
    con.rollback()
    print('transaction rollbacked due to error:',str(e))
con.close()