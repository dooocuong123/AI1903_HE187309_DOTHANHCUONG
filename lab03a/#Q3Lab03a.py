#Q3Lab03a
#1 Create a string made of the middle four characters
s1 = "BillDesctran"
s2 = "HoSongHu"
middle1 = s1[len(s1)//2-2:len(s1)//2+2]
middle2 = s2[len(s2)//2-2:len(s2)//2+2]
print(f"Original String is {s1}")
print(f"Middle four chars are: {middle1}")
print(f"Original String is {s2}")
print(f"Middle four chars are: {middle2}")

#2 Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in
# the middle of s1.
s1 = "Ault"
s2 = "Kelly"
n = len(s1)//2
s3 = s1[:n]+s2+s1[n:]
print(s3)

# #3 Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s
# first, middle, and last characters.
s1 = "America"
s2 = "Japan"
n1 = len(s1)//2 + 1
n2 = len(s2)//2 + 1
s3 = s1[:1] + s2[:1] + s1[n1-1:n1] + s2[n2-1:n2] + s1[len(s1)-1:len(s1)]+s2[len(s2)-1:len(s2)]
print(s3)

#4 Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
capitalization = ""
lowercase = ""

for char in str1:
    if char.isupper():
        capitalization += char
    else:
        lowercase += char

n = lowercase + capitalization
print(n)
#5 Count all letters, digits, and special symbols from a given string
str = input("String: ")
numberOfLetters = 0
numberOfDigits = 0
numberOfOthers = 0
for i in range(len(str)):
    if('0'<= str[i] and str[i]<='9'): numberOfDigits += 1
    elif ('a'<= str[i] and str[i]<='z') or ('A'<= str[i] and str[i]<='Z'): numberOfLetters += 1
    else: numberOfOthers += 1
chars1 = numberOfDigits + numberOfLetters
print(f"Chars = {chars1} " )
print(f"Digits = {numberOfDigits} " )
print(f"Symbol = {numberOfOthers} " )
