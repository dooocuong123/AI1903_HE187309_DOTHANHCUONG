# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Employee:
    id = 0
    name = ''
    salary = 0
    age = 0
    
    def inputEmployee(self):
        self.id = int(input('Enter employees: '))
        self.name =  input('Enter name: ')
        self.salary =  int(input('Enter salary: '))
        self.age = int(input('Enter age: '))
        
    def printEmployee(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Age: {self.age}")
        
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST EMPLOYEE========
    def InputListEmployee(self):
        n = int(input('Enter the number of employees: '))
        lst = []
        for i in range(n):
            e = Employee()
            e.inputEmployee()
            lst.append(e)
        return lst
        
        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================
        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for x in employeeList:
            x.printEmployee()
        # end def


    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        employeeList.sort(key = lambda x: x.age, reverse = True)
        for x in employeeList:
            x.printEmployee()
        # end def



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        lst = [x for x in employeeList if x.age >= 18]
        lst.sort(key=lambda x: x.salary, reverse=True)
        for x in lst:
            x.printEmployee()
        # end def
#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        else:
            print("Wrong select")
        print("FINISH")

main = Main()
main.main()
