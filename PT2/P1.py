def replace_chars(string, char1, char2):
    replaced_string = ''
    for char in string:
        if char == char1:
            replaced_string += char2
        else:
            replaced_string += char
    return replaced_string

def main():
    user_input = input("Enter a string: ")
    char1 = input("Enter the character to replace: ")[0]
    char2 = input("Enter the replacing character: ")[0]

    result = replace_chars(user_input, char1, char2)
    print("Result:", result)

if __name__ == "__main__":
    main()
