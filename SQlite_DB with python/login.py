import sqlite3

class LoginApplication:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                username TEXT NOT NULL UNIQUE,
                                password TEXT NOT NULL
                            )''')
        self.conn.commit()

    def register_user(self, username, password):
        try:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            self.conn.commit()
            print("Registration successful!")
        except sqlite3.IntegrityError:
            print("Username already exists. Please choose a different username.")

    def authenticate_user(self, username, password):
        self.cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = self.cursor.fetchone()
        if result:
            stored_password = result[0]
            if stored_password == password:
                print("Authentication successful!")
            else:
                print("Authentication failed. Invalid username or password.")
        else:
            print("Authentication failed. Invalid username or password.")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed.")


# Example usage
login_app = LoginApplication("C:/SQLite3/student")

# Registering users
login_app.register_user("john_doe", "password123")
login_app.register_user("jane_smith", "securepassword")

# Authenticating users
login_app.authenticate_user("john_doe", "password123")
login_app.authenticate_user("john_doe", "wrongpassword")
login_app.authenticate_user("jane_smith", "securepassword")

login_app.close_connection()
