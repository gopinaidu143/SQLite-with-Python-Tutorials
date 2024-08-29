class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def cal_emp_salary(self, hours_worked):
        if hours_worked <= 50:
            return self.emp_salary
        else:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary / 50))
            return self.emp_salary + overtime_amount

    def emp_assign_dep(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)



employees_data = [
    ("ADAMS", "E7876", 50000, "ACCOUNTING"),
    ("JONES", "E7499", 45000, "RESEARCH"),
    ("MARTIN", "E7900", 50000, "SALES"),
    ("SMITH", "E7698", 55000, "OPERATIONS")
]

employees = []
for emp_data in employees_data:
    emp = Employee(*emp_data)
    employees.append(emp)


print("Original Employee Details:")
for emp in employees:
    emp.print_employee_details()

employees[1].emp_assign_dep("MARKETING")

overtime_hours = 55
overtime_salary = employees[3].cal_emp_salary(overtime_hours)

print("\nUpdated Employee Details:")
for emp in employees:
    emp.print_employee_details()

print("\nOvertime Salary for Employee 'SMITH' with 55 hours worked:", overtime_salary)
