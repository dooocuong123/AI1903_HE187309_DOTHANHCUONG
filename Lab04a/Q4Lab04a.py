import os
import shutil
#1 Rename a file after checking whether it exists
def rename_a_file(old_name):
    if os.path.exists(old_name):
        new_name = "new_"+old_filename
        os.rename(old_name, new_name)
        print(f"File '{old_name}' has been renamed to '{new_name}'.")
    else:
        print(f"File '{old_name}' does not exist.")

old_filename = "details.txt"
rename_a_file(old_filename)


#2 Rename Multiple Files in Python
def rename_multiple_file(list):
    for namefile in list:
        rename_a_file(namefile)

my_list = ['apple.txt','orange.txt','banana.txt']
rename_multiple_file(my_list)

#3 Renaming only a list of files in a folder
def rename_only_a_list_of_file_in_a_folder(list):

    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return
    
    for filename in file_list:
        old_path = os.path.join(folder_path, filename) 
        new_path = os.path.join(folder_path, filename)
        
        try:
            os.rename(old_path, new_path)  # Đổi tên file
            print(f"File '{old_path}' has been renamed to '{new_path}'.")
        except FileNotFoundError:
            print(f"File '{old_path}' does not exist.")
        except FileExistsError:
            print(f"File '{new_path}' already exists.")

my_list = ['apple.txt','orange.txt','banana.txt']
my_directory = "C:/Users/ADMINS/Desktop/lab4/files"
rename_multiple_file(my_list)


#4 Renaming files with a timestamp
def rename_files_with_a_timestamp(old_name):
    if os.path.exists(old_name):
        import datetime
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime("%d-%b-%Y")
        new_name = f"{formatted_date}.txt"
        os.rename(old_name, new_name)
        print(f"File '{old_name}' has been renamed to '{new_name}'.")
    else:
        print(f"File '{old_name}' does not exist.")


#5 Renaming the Extension of the Files
def rename_files_in_directory(directory, old_suffix, new_suffix):
    try:
        files = os.listdir(directory)
        for filename in files:
            if filename.endswith(old_suffix):
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, filename.replace(old_suffix, new_suffix))  
                os.rename(old_path, new_path) 
                print(f"File '{old_path}' has been renamed to '{new_path}'.")
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")

my_directory = "C:/Users/ADMINS/Desktop/lab4/files"
my_old_suffix = ".txt"
my_new_suffix = ".csv"

rename_files_in_directory(my_directory, my_old_suffix, my_new_suffix)

#6 Renaming and then moving a file to a new location
def rename_and_move_file(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        
        shutil.move(new_path, "new_directory_path")
        
        print(f"File '{old_path}' has been renamed and moved to '{new_path}' in the new location.")
    except IOError as e:
        print(f"An error occurred: {e}")


my_old_path = "C:/Users/ADMINS/Desktop/lab4/files"
my_new_path = "C:/Users/ADMINS/Desktop/lab4/files"
rename_and_move_file(my_old_path, my_new_path)


