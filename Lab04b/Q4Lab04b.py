def hash_display(filename):
    try :
        with open(filename, 'r',encoding = 'utf = 8') as file:
            content = file.read()
            formatted_content = '#'.join(content)
            print(formatted_content)
    except IOError:
        print("Error could not hash display # "+filename)

def JTOI(filename):
    try:
        corrected_text = ""
        with open(filename, 'r',encoding = 'utf = 8') as file:
            for line in file:
                corrected_line = line.replace('J', 'I')
                corrected_text += corrected_line
        print(corrected_text)
    except IOError:
        print("Error could not change J to I "+filename)
if __name__ == '__main__':
    #1  a symbol "# separates every next character."
    # Write a function definition for hash_display()
    filename1 = "matter.txt"
    hash_display(filename1)
    #2 change J to I.
    # write a function fefinition for JTOI()
    filename2 = "WORDS.TXT"
    JTOI(filename2)
