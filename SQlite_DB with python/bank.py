import sqlite3


class BankApplication:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                balance REAL NOT NULL
                            )''')
        self.conn.commit()

    def create_account(self, name, balance):
        self.cursor.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', (name, balance))
        self.conn.commit()
        print("Account created successfully!")

    def get_balance(self, account_id):
        self.cursor.execute('SELECT balance FROM accounts WHERE id = ?', (account_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            print("Account not found!")

    def deposit(self, account_id, amount):
        current_balance = self.get_balance(account_id)
        if current_balance is not None:
            new_balance = current_balance + amount
            self.cursor.execute('UPDATE accounts SET balance = ? WHERE id = ?', (new_balance, account_id))
            self.conn.commit()
            print("Deposit successful!")
            print("New balance:", new_balance)

    def withdraw(self, account_id, amount):
        current_balance = self.get_balance(account_id)
        if current_balance is not None:
            if current_balance >= amount:
                new_balance = current_balance - amount
                self.cursor.execute('UPDATE accounts SET balance = ? WHERE id = ?', (new_balance, account_id))
                self.conn.commit()
                print("Withdrawal successful!")
                print("New balance:", new_balance)
            else:
                print("Insufficient balance!")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed.")


# Example usage
bank = BankApplication("C:/SQLite3/student")
bank.create_account("John Doe", 500.0)
account_id = 1
bank.deposit(account_id, 100.0)
bank.withdraw(account_id, 50.0)
print("Current balance:", bank.get_balance(account_id))
bank.close_connection()
