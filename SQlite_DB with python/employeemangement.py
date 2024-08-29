import sqlite3


class admin:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.create_admin_table()

    def create_admin_table(self):
        self.cur.execute('''
            create table if not exists admin (
                id integer primary key,
                name text(50) not null,
                password text(50) not null unique
            )'''
                         )
        self.con.commit()

    def admin_registration(self, name, password):
        try:
            self.cur.execute('insert into admin (name, password) values (?, ?)', (name, password))
            self.con.commit()
            print('Admin successfully registered!')
        except sqlite3.IntegrityError:
            print('User already exists! Try with other valid input.')

    def admin_verification(self, name, password):
        self.cur.execute('select name from admin where name=? and password=?', (name, password))
        result = self.cur.fetchone()
        if result:
            print('Successfully logged in:', result)
            return True
        else:
            print('Invalid username or password! Try again with correct credentials.')
            return False

    def create_employee_table(self):
        self.cur.execute('''
            create table if not exists employee (
                id integer primary key,
                name text(50) not null,
                salary int not null,
                designation text(50),
                performance int not null
            )'''
                         )
        self.con.commit()
        print('Employee table successfully created!')

    def insert_employee(self):

        name = input('Enter employee name: ')
        salary = int(input('Enter employee salary: '))
        designation = input('Enter employee role: ')
        performance = int(input('Rate the employee performance range (1-10): '))
        data = (name, salary, designation, performance)
        self.cur.execute('insert into employee(name,salary,designation,performance) values (?, ?, ?, ?)', data)
        self.con.commit()
        print('Successfully inserted employee data!')

    def delete_employee(self):
        self.cur.execute('select * from employee where performance <= 3')
        delete_data = self.cur.fetchall()
        print("Employee data whose performance <= 3:")
        print(delete_data)
        self.cur.execute('delete from employee where performance <= 3')
        self.con.commit()
        print('Successfully deleted!')

    def update_employee(self):
        self.cur.execute('select * from employee where performance >= 9')
        update_data = self.cur.fetchall()
        print("Employee data whose performance >= 9:")
        print(update_data)
        update_salary = int(input('Enter updated salary: '))
        self.cur.execute('update employee set salary=? where performance >= 9', (update_salary,))
        self.con.commit()
        print('Updated successfully!')

    def view_employee(self):
        self.cur.execute('select * from employee')
        result = self.cur.fetchall()
        for row in result:
            print(row)


# Example usage:
admin_obj = admin("C:/SQLite3/student.db")
# Replace with your desired database file path.
admin_obj.admin_registration('abhi', '123')

username = input('enter admin username:')
password = input('enter admin password:')
if admin_obj.admin_verification(username,password):
    while True:
        print('Perform operations:')
        print('1) Create employee table')
        print('2) Insert employee data')
        print('3) Delete employee data')
        print('4) Update employee data')
        print('5) View employee data')
        print('6) Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            admin_obj.create_employee_table()
        elif choice == 2:
            admin_obj.insert_employee()
        elif choice == 3:
            admin_obj.delete_employee()
        elif choice == 4:
            admin_obj.update_employee()
        elif choice == 5:
            admin_obj.view_employee()
        elif choice == 6:
            break
        else:
            print('Invalid choice! Try again.')
else:
    print('invalid username or password!')