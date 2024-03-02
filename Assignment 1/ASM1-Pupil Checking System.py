class Pupil:
    def __init__(self, roll_number, name, mark_E, mark_M, mark_P, mark_C, mark_CS):
        self.roll_number = roll_number
        self.name = name
        self.mark_E = mark_E
        self.mark_M = mark_M
        self.mark_P = mark_P
        self.mark_C = mark_C
        self.mark_CS = mark_CS
        
class PupilManagementSystem:
    def __init__(self):
        self.pupils = []
    def name_property(self,i):
        list_properties = ["roll number","name","English","Maths","Physics","Chemistry","CS"]
        return list_properties[i]
    
    def loop_create_pupil(self):
        while True:
            try:
                self.create_pupil_record()
                more = input("Wants to enter more record (y/n)?: ")
                if more.lower() == 'n':
                    break
                elif more.lower() == 'y':
                    continue
                else:
                    print("Error choice, please try again")
            except ValueError:
                print("Invalid input. Please enter a valid value.")

    def create_pupil_record(self):
        roll_number = int(input("Enter roll number: "))
        name = input("Enter name: ")
        mark_E = self.input_mark("English")
        mark_M = self.input_mark("Maths")
        mark_P = self.input_mark("Physics")
        mark_C = self.input_mark("Chemistry")
        mark_CS = self.input_mark("CS")
        pupil = Pupil(roll_number, name, mark_E, mark_M, mark_P, mark_C, mark_CS)
        self.pupils.append(pupil)
        
    def input_mark(self, subject):
        while True:
            try:
                mark = int(input(f"Enter Marks in {subject}: "))
                if 0 <= mark <= 10:
                    return mark
                else:
                    print("Invalid mark. Mark should be between 0 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def display_all_pupil_records(self):
        print("\nPUPIL DETAILS..")
        for pupil in self.pupils:
            print(f"Roll Number: {pupil.roll_number}")
            print(f"Name: {pupil.name}")
            print(f"English: {pupil.mark_E}")
            print(f"Maths: {pupil.mark_M}")
            print(f"Physics: {pupil.mark_P}")
            print(f"Chemistry: {pupil.mark_C}")
            print(f"CS: {pupil.mark_CS}")
            
    def search_pupil_record(self):
        roll_number = int(input("Enter the rollno you want to search: "))
        found = False
        for pupil in self.pupils:
            if pupil.roll_number == roll_number:
                found = True
                print("\nPUPIL DETAILS..")
                print(f"Roll Number: {pupil.roll_number}")
                print(f"Name: {pupil.name}")
                print(f"English: {pupil.mark_E}")
                print(f"Maths: {pupil.mark_M}")
                print(f"Physics: {pupil.mark_P}")
                print(f"Chemistry: {pupil.mark_C}")
                print(f"CS: {pupil.mark_CS}")
                break
        if not found:
            print("Pupil not found.")
                
    def modify_pupil_record(self):
        print("\nMODIFY RECORD")
        roll_number = int(input("Enter roll number: "))
        for pupil in self.pupils:
            if pupil.roll_number == roll_number:
                pupil.name = self.edit_pupil_details(pupil.name, "name")
                pupil.mark_E = self.edit_pupil_details(pupil.mark_E, "English")
                pupil.mark_M = self.edit_pupil_details(pupil.mark_M, "Maths")
                pupil.mark_P = self.edit_pupil_details(pupil.mark_P, "Physics")
                pupil.mark_C = self.edit_pupil_details(pupil.mark_C, "Chemistry")
                pupil.mark_CS = self.edit_pupil_details(pupil.mark_CS, "CS")
                print("Record updated")
                break
        else:
            print("Pupil not found.")

    def edit_pupil_details(self, current_value, property_name):
        while True:
            print(f"{property_name}: {current_value}")
            choice = input("Wants to edit(y/n)? ").lower()
            if choice == 'y':
                new_value = input(f"Enter new {property_name}: ")
                return new_value
            elif choice == 'n':
                return current_value
            else:
                print("Error choice please choose again")
        
    def delete_pupil_record(self):
        print("\nDELETE RECORD")
        roll_number = int(input("Enter roll number: "))
        self.display_all_pupil_records()
        for pupil in self.pupils:
            if pupil.roll_number == roll_number:
                self.pupils.remove(pupil)
                print("record found and deleted.")
                break
        else:
            print("Pupil not found.")
            
    def display_class_result(self):
        print("\nCLASS RESULT")
        print("Rollno\tName\tEnglish\tMaths\tPhysics\tChemistry\tCS")
        for pupil in self.pupils:
            print(f"{pupil.roll_number}\t{pupil.name}\t{pupil.mark_E}\t{pupil.mark_M}\t{pupil.mark_P}\t{pupil.mark_C}\t{pupil.mark_CS}")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. CREATE PUPIL RECORD")
            print("2. DISPLAY ALL PUPILS RECORDS")
            print("3. SEARCH PUPIL RECORD")
            print("4. MODIFY PUPIL RECORD")
            print("5. DELETE PUPIL RECORD")
            print("6. BACK TO MAIN MENU")
            choice = input("Enter choice(1-6): ")

            if choice == '1':
                self.loop_create_pupil()
            elif choice == '2':
                self.display_all_pupil_records()
            elif choice == '3':
               self.search_pupil_record()
            elif choice == '4':
               self.modify_pupil_record()
            elif choice == '5':
               self.delete_pupil_record()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def report_menu(self):
        while True:
            print("\nReport Menu:")
            print("1. CLASS RUSULT")
            print("2. PUPIL REPORT CARD")
            print("3. BACK TO MAIN MENU")
            choice = input("Enter choice (1-3): ")
            if choice =='1':
                self.display_class_result()
            elif choice =='2':
                self.search_pupil_record()
            elif choice =='3':
                break
            else:
                print("Error choice. please try again")

    def main_menu(self):
        while True:
            print("\nMAIN MENU:")
            print("1. REPORT MENU")
            print("2. ADMIN MENU")
            print("3. EXIT")
            choice = input("Enter choice(1-3): ")
            if choice == '1':
                self.report_menu()
            elif choice == '2':
                self.admin_menu()
            elif choice == '3':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

# Main program
if __name__ == "__main__":
    system = PupilManagementSystem()
    system.main_menu()
