#Q1
#1 Creating a list in Python
def creating_list():
    try:
        input_string = input()
        string_list = input_string.split()
        string_list = [x for x in string_list]
        print(string_list)
    except IOError:
        print("Error: Could not run creating_list")
#2 Concatenate two lists index-wise
def Concatenate_two_lists():
    try:
        list1 = ["M","na","i","Ke"]
        list2 = ["y","me","s","lly"]
        list3 =[]
        for i in range(0,len(list1)):
            list3.append(list1[i]+list2[i])
        print(list3)
    except IOError:
        print("Error: Could not run concatenate_two_lists")
if __name__ == "__main__":
    creating_list()
    Concatenate_two_lists()