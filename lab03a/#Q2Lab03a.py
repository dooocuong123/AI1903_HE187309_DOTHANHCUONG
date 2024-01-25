# Q2 lab03a
# 1 Write a program to print the following number pattern using a loop
# Initial list
list1 = [75, 76, 150, 155, 145, 654, 600, 100]
for i in list1:

    # If the number is greater than 500, then stop the loop
    if i > 500:
        break

    # If the number is greater than 150, then skip it and move to the next number
    if i > 150:
        continue

    # Convert the list into numbers that must be divisible by 5
    if i%5==0:
        list2 =[i]
        for j in list2:
            print(j)

# 2 Count the total number of digits in a number

number = str(input("Enter integer number: "))
cout =len(number)
print(f"Total digits are: {cout}")

# 3 Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in list1[0:]:
    print(i)
