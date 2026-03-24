# Employee Management System


# Step 1: Sample Employee Data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Kundan', 'age': 25, 'department': 'IT', 'salary': 60000},
    103: {'name': 'Amit', 'age': 30, 'department': 'Finance', 'salary': 55000}
}

# ==========================
# Add Employee Function
# ==========================
def add_employee():
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("Employee ID already exists! Please enter a unique ID.")
                continue
            break
        except ValueError:
            print("Invalid input! Employee ID must be an integer.")

    name = input("Enter Employee Name: ")

    while True:
        try:
            age = int(input("Enter Employee Age: "))
            break
        except ValueError:
            print("Invalid input! Age must be a number.")

    department = input("Enter Employee Department: ")

    while True:
        try:
            salary = float(input("Enter Employee Salary: "))
            break
        except ValueError:
            print("Invalid input! Salary must be a number.")

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print(f"Employee {name} (ID: {emp_id}) added successfully!")

# ==========================
# View All Employees
# ==========================
def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\n--- Employee List ---")
    print("{:<10} {:<15} {:<5} {:<12} {:<10}".format('ID', 'Name', 'Age', 'Department', 'Salary'))
    print("-" * 55)
    for emp_id, details in employees.items():
        print("{:<10} {:<15} {:<5} {:<12} {:<10}".format(
            emp_id,
            details['name'],
            details['age'],
            details['department'],
            details['salary']
        ))
    print("-" * 55)

# ==========================
# Search Employee by ID
# ==========================
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print("\nEmployee Found:")
            print(f"ID: {emp_id}")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary: {details['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input! Employee ID must be an integer.")

# ==========================
# Step 2: Menu System
# ==========================
while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        print("Thank you for using Employee Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")