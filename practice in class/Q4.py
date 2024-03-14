def most_frequent_word(sentence):
    words = sentence.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    max_count = 0
    most_frequent = ""
    
    for word, count in word_count.items():  # Sửa từ 'item()' thành 'items()' để lặp qua tất cả các cặp từ và số đếm
        if count > max_count:
            max_count = count
            most_frequent = word
            
    return most_frequent, max_count

def read_file(file_path):
    try:
        with open(file_path) as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("Error: File not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    while True:
        file_path = input("Enter file: ")
        content = read_file(file_path)
        
        if content is None:
            break
        
        result = most_frequent_word(content)
        most_frequent, count = result
        print(f"The most frequent word is '{most_frequent}' with count {count}")
        break

main()
