def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)
def count_the_number_of_lines(filename):
    try:
        count = 0
        with open(filename, 'r', encoding = 'utf-8')as f:
            for line in f:
                cleaned_line = line.strip()
                if cleaned_line and not cleaned_line.startswith('T'):
                    count += 1
        print(f"No of lines not starting with 'T' = {count}")
        
    except IOError:
        print("Error: could not count the number of lines " + filename)
            
if __name__=='__main__':
    #1 read the content from a text file "poem.txt"
    # line by line and display the same on-screen.
    namefile1 = "poem.txt"
    read_file(namefile1)
    #2 count the number of lines from a text file "story.txt,"
    # which is not starting with an alphabet "T."
    namefile2 = "story.txt"
    count_the_number_of_lines(namefile2)
    
