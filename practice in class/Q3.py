from datetime import datetime
def simple_menu():
    print("1-Processing date data")
    print("2-Character data")
    print("3-Quit")


def is_true_day(day, month, year):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def ascii_code(string):
    print("Output")
    for char in string:
        ascii_code = ord(char)
        hexadecimal = hex(ascii_code)
        print(char,ascii_code, hexadecimal)

def main():
    while True:
        simple_menu()
        n = int(input())
        if n == 1:   
            day =  int(input(f"day:"))
            month =  int(input(f"month:"))
            year =  int(input(f"year:"))
            result = is_true_day(day, month, year)
            if result == True:
                print("True day")
            else:
                print("Error day")
        elif n == 2:
            string = input("Enter a string: ")
            ascii_code(string)
        elif n == 3:
            print("Thank you for using this program.")
            break
        else:
            print("Error, please choose again!")

main()
