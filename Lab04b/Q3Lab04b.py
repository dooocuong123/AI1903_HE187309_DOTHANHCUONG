def count_uppercase_characters(filename):
    try:
        count = 0
        with open(filename, 'r',encoding = 'utf = 8') as file:
            text = file.read()
            for char in text:
                if char.isupper():
                    count += 1
        print(count)
    except IOError:
        print("Error could not count uppercase characters "+filename)
def count_this_and_these(filename):
    try:
        words_count = 0
        with open(filename, 'r',encoding = 'utf = 8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if word.lower() == 'this':
                        words_count += 1
                    elif word.lower() == 'these':
                        words_count += 1
        print(words_count)
    except IOError:
        print("Error could not count this and these "+filename)
if __name__ == '__main__':
    #1 count uppercase characters in a text file.
    filename1 = "story.txt"
    count_uppercase_characters(filename1)
    #2 count the words "this" and "these" present
    # in a text file "article.txt". 
    filename2 = "article.txt"
    count_this_and_these(filename2)


