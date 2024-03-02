#Q5
def count_letters(input_line):
    letter_count = {}

    for letter in input_line:
        if letter.isalpha():
            letter = letter.lower()
            letter_count[letter] = letter_count.get(letter, 0) + 1

    return letter_count

def main():
    input_line = input("Enter a line of text: ")

    letter_count = count_letters(input_line)

    print("Letter counts:")
    for letter, count in sorted(letter_count.items()):
        print(f"The letter '{letter}' appears {count} time(s).")

if __name__ == "__main__":
    main()
