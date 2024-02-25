#1
def write_to_new_file(file_name, content_write):
    try:
        with open(file_name, 'w', encoding = 'utf-8') as file:
            file.write(content_write)
            
        print("Done Writing")
        
        with open(file_name, 'r', encoding = 'utf-8') as file:
            print(file.read())
    except IOError:
        print("Error: could not use file.")
        
if __name__ == "__main__":
    filename = "new_file.txt"
    data_write = "This is new content"
    write_to_new_file(filename, data_write)

#2
def write_to_existing_file(file_name, data):
    try:
        print("Openning file again..")
        with open(file_name, 'w', encoding = 'utf-8') as file:
            file.write(data)
        
        with open(file_name, 'r', encoding = 'utf-8') as file:
            print(file.read())
    except IOError:
        print("Error: could not use file.")

if __name__ == "__main__":
    filename = "existing_file.txt"
    data_to_write = "This is overwritten content."
    write_to_existing_file(filename, data_to_write)
#3 Write a list of lines to a file
def write_lines_to_file(file_name, lines):
    try:
        with open(file_name, 'w', encoding = 'utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        with open(file_name, 'r', encoding = 'utf-8') as file:
            print(file.read())

    except IOError:
        print("Error: could not use file.")

if __name__ == "__main__":
    lines_to_write = [
        "Name: Emma",
        "Address: 221 Baker Street",
        "City: London"
    ]
    filename = "output.txt"
    write_lines_to_file(filename, lines_to_write)




