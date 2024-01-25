# Q1Lab03a
# 1 a program to print the following number pattern using a loop.
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 2 Calculate the sum of all numbers from 1 to a given number
n = int(input("Enter number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(f"Sum is: {sum}")