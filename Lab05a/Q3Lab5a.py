#Q3
#1 Merge two Python dictionaries into one
def Q3_1():
    dict1 = {'Ten':10,'Twenty':20,'Thirty':30}
    dict2 = {'Thirty':30,'Fourty':40,'Fifity':50}
    result = {**dict1,**dict2}
    print(result)


#2 Print the value of key ‘history’ from the below dict
def Q3_2():
    sampleDict = {
        "class":{
            "student":{
                "name":"Mike",
                "marks":{
                    "physics":70,
                    "history":80
                    }
                }
            }
        }

    print(sampleDict["class"]["student"]["marks"]["history"])


#3 Initialize dictionary with default values
def Q3_3():
    employees = ['Kelly','Emma']
    defaults = {"Designation":'Developer',"salary":8000}
    my_dict = {employee: defaults.copy() for employee in employees}
    print(my_dict)
    
if __name__=="__main__":
    Q3_1()
    Q3_2()
    Q3_3()
    