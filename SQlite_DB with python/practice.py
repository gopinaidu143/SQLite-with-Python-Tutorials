import sqlite3


class bank:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''create table if not exists accounts(id INTEGER primary key,
        name text(50) not null,balance real not null)''')
        self.con.commit()

    def create_account(self, name, amount):
        self.cur.execute('insert into accounts (name,balance) values(?,?)', (name, amount))
        self.con.commit()
        print('account created successfully!!')
    def get_balance(self,account_id):
        self.cur.execute( 'select balance from accounts where id=?',(account_id,))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            print('invalid account_id!!')
    def deposit(self,account_id,amount):
        current_balance = self.get_balance(account_id)
        if current_balance is not None:
             new_balance = current_balance+amount
             self.cur.execute( 'update accounts set balance=? where id=?',(new_balance,account_id))
             self.con.commit()
             print('amount deposited successfully. current balance:',new_balance)
        else:
            print('account not found!!')
    def withdraw(self,account_id,amount):
        current_balance = self.get_balance(account_id)
        if current_balance is not None:
            if current_balance>=amount:
                new_balance = current_balance-amount
                self.cur.execute('update accounts set balance=? where id=?',(new_balance,account_id))
                self.con.commit()
                print('withdraw successful.current balance:',new_balance)
            else:
                print('insufficient balance!!')
        else:
            print('account not found!!')
    def close_con(self):
        self.cur.close()
        self.con.close()
        print('successfully connection closed!!')
bank_app = bank("C:/SQLite3/student")
bank_app.create_account('gopi',500)
account_id=1
bank_app.deposit(account_id,500)
bank_app.withdraw(account_id,300)
bank_app.close_con()









