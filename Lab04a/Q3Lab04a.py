def the_begginning_of_file(file_name):
    try:
        with open(file_name, "r", encoding = 'utf=8') as file:
            file.seek(0)
            data = file.read()
            print(data)
    except IOError:
        print("Error1")
def the_end_of_file(file_name):
    try:
        with open(file_name, "r",encoding = 'utf=8') as file:
            file.seek(0, 2)  # Move the file pointer to the end
            data = file.read()
            print("This content is added to the end of the file")
            print(data)
    except IOError:
        print("Error2")
def from_the_current_position(file_name):
    try:
        with open(file_name, "r",encoding = 'utf=8') as file:
            lines = file.readlines()

        for line in lines:
            words = line.split()
            if len(words) >= 2:
                print(words[1])
    except IOError:
        print("Error 3")
def backward_with_negative_offset(file_name):
    try:
        f = open(file_name, "rb")
        content = f.read()
        content_1 = content[:8]
        print(content_1.decode('utf-8'))
 
        f.seek(3)
        print(f.readline().decode('utf-8'))
        f.close()
    
            
    except IOError:
        print("Error 4")

def get_file_handle_position(file_name, my_content):
    try:
        with open(file_name, "r+",encoding = 'utf=8') as f:
            f.seek(75)
            print("file handle at:", f.tell())
            f.seek(95)
            print("file handle at:", f.tell())
            f.seek(0)
            print("file handle at:", f.tell())
            print("***Printing File Content***")
            print(f.read())
            f.write(my_content)
            print("This content is added to the end of the file")
            print(my_content)
            print("***Done***")
            f.seek(95)
            print("file handle at:", f.tell())
    except IOError:
        print("Error occurred while accessing the file.")




filename = "test.txt"       
the_begginning_of_file(filename)
the_end_of_file(filename)
from_the_current_position(filename)
backward_with_negative_offset(filename)

add_content = "Demonstrating tell"
get_file_handle_position(filename, add_content)





