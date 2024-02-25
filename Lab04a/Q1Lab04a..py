#Q1
from datetime import datetime
import os
# 1 Create a new empty text file named ‘sales.txt’
def create_file_name():
    try:
        file_path = 'sales.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("Used variable file")
        print(f"Created {file_path}")
    except IOError:
        print("Error: could not creae file name" + filename)

# 2 Create File with a DateTime
def create_file_datetime():
    try:
        current_datetime = datetime.now().strftime("%d-%m-%Y")
        file_name = f"{current_datetime}.txt"
        with open(file_name, "w", encoding='utf-8') as file:
            file.write("Used variable file")
        print(f"Created {file_name}")
    except IOError:
        print("Error: Could not create file datetime")
    
def create_file_datetime_and_time():
    try:
        current_datetime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        file_name = f"{current_datetime}.txt"
        with open(file_name, "w", encoding='utf-8') as file:
            file.write("Used variable file")
        print(f"Created {file_name}")
    except IOError:
        print("Error: Could not create file datetime and time")
        
def create_file_in_directory(directory_path):
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        current_datetime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        file_name = os.path.join(directory_path, f"{current_datetime}.txt")
        with open(file_name, "w", encoding='utf-8') as file:
            file.write("Used variable file")
        print(f"Created {file_name}")
    except IOError:
        print("Error: Could not create file in directory")

#3 Create a file with Permission
def create_file(filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)
 
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)
 
def append_file(filename, text):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)
 
def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)
 
 
if __name__ == '__main__':
    #1  Create a new empty text file named ‘sales.txt’
    create_file_name()
    #2 Create File with a DateTime
    create_file_datetime()
    
    create_file_datetime_and_time()
    
    directory_mypath = r"C:\Excercises\\"
    create_file_in_directory(directory_mypath)
    
    #3 Create a file with Permission.
    filename_example = "example.txt"
    new_filename_example = "new_example.txt"
 
    create_file(filename_example)
    read_file(filename_example)
    append_file(filename_example, "This is some additional text.\n")
    read_file(filename_example)
    rename_file(filename_example, new_filename_example)
    # after renamed we need create new file
    create_file(filename_example)
    read_file(filename_example)
    delete_file(filename_example)
    delete_file(new_filename_example)

