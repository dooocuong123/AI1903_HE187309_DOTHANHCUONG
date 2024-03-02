#Q4
def Q4_1():
    my_tuple = ("Orange", [10, 20, 30], (5, 15, 25))
    output = my_tuple[1][1]
    print(output)
def Q4_2():
    tuple1 =(10,20,30,40)
    for i in range(0,len(tuple1)):
        count = chr(97 + i)
        print(f"print({count}) # should print {tuple1[i]}")
def Q4_3():
    tuple1 = (11,22)
    tuple2 = (99,88)
    tuple1,tuple2 = tuple2,tuple1
    print(f"tuple1: {tuple1}")
    print(f"tuple2: {tuple2}")
if __name__=="__main__":
    Q4_1()
    Q4_2()
    Q4_3()