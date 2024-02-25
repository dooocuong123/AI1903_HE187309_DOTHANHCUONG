def count_words_in_file(filename):
    try:
        with open(filename, 'r',encoding = 'utf = 8') as file:
            text = file.read()
            total_words = len(text.split())
        print("Total number of words in the file:", total_words)
    except IOError:
        print("Error: could not count words in file" +filename)


def display_words(filename):
    try:
        with open(filename, 'r',encoding = 'utf = 8') as file:
            for line in file:
                words = line.split()
                filtered_words = [word for word in words if len(word) < 4]
                if filtered_words:
                    print(' '.join(filtered_words), end=' ')
    except IOError:
        print("Error could not display words in "+filename)

if __name__ == '__main__':
    #1 count and display the total number of words in a text file.
    filename1 = "story.txt"
    count_words_in_file(filename1)
    #2 Write a function display_words()
    # read lines from a text file "story.txt" and display
    # those words less than 4 characters.
    filename2 = "story.txt"
    display_words(filename2)

