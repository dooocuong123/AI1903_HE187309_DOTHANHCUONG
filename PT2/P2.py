import os

def add_employee(code, name, salary, allowance):
    with open('input.txt', 'a') as file:
        file.write(f"{code},{name},{salary},{allowance}\n")

def search_employee_by_name(name):
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        employees = [line.strip().split(",") for line in lines]
        left, right = 0, len(employees) - 1
        while left <= right:
            mid = (left + right) // 2
            if employees[mid][1] == name:
                return employees[mid]
            elif employees[mid][1] < name:
                left = mid + 1
            else:
                right = mid - 1
        return None

def remove_employee_by_code(code):
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    with open('input.txt', 'w') as file:
        for line in lines:
            if line.split(',')[0] != code:
                file.write(line)

def sort_and_save():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        employees = [line.strip().split(",") for line in lines]
        employees.sort(key=lambda x: int(x[2]) + int(x[3]), reverse=True)
    with open('result.txt', 'w') as file:
        for employee in employees:
            file.write(','.join(employee) + '\n')

def main():
    while True:
        print("\n1. Add new employee")
        print("2. Find employee by name")
        print("3. Remove employee by code")
        print("4. Print sorted list by salary + allowance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            code = input("Enter employee code: ")
            name = input("Enter employee name: ")
            salary = input("Enter employee salary: ")
            allowance = input("Enter employee allowance: ")
            add_employee(code, name, salary, allowance)
            print("Employee added successfully.")
        elif choice == '2':
            name = input("Enter employee name to search: ")
            employee = search_employee_by_name(name)
            if employee:
                print("Employee found:", ','.join(employee))
            else:
                print("Employee not found.")
        elif choice == '3':
            code = input("Enter employee code to remove: ")
            remove_employee_by_code(code)
            print("Employee removed successfully.")
        elif choice == '4':
            sort_and_save()
            print("List sorted by salary + allowance and saved to result.txt.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
