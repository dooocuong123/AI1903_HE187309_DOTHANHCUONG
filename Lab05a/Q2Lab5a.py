#Q2

def input_str():
    input_string =  input("Enter list ")
    string_list =  input_string.split()
    string_list_1 = [count for count in string_list]
    print(string_list_1)
    return string_list_1
#1 Turn every item of a list into its square
def its_square(numbers):
    try:
        print(numbers)
        square = [int(i**2) for i in numbers]
        print(square)
    except IOError:
        print("Error: Could not use its_square")
if __name__=="__main__":
    numbers = input_str()
    if numbers == []:
        numbers = [1,2,3,4,5,6,7]
    its_square(numbers)
#2 Concatenate two lists in the following order
def two_list(list1,list2):
    for i in range(0,len(list1)):
        list3.append(list1[i]+" "+list2[i])
    print(list3)
    
if __name__=="__main__":
    list1 = input_str()
    list2 = input_str()
    if list1==[] or list2==[]:
        list1 = ["Hello","take"]
        list2 = ["Dear","Sir"]
    list3 = []
    two_list(list1,list2)