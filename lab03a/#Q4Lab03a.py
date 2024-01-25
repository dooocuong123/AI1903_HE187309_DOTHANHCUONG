#Q4Lab03a
#1 Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
result = ""
for i in range(len(str1)):
    if('0'<= str1[i] and str1[i]<='9'):
        result += str1[i]
print(int(result))

#2 Remove special symbols / punctuation from a string
str1 = "/*Jon is @developer & musician"
result = ""
for i in range(len(str1)):
    if('a'<= str1[i] and str1[i]<='z') or ('A'<= str1[i] and str1[i]<='Z'or (" "==str1[i])):
        result += str1[i]
print(result)

#3 Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Keylly", None, "Eric", ""]
list2 = [s for s in str_list if s and any(c.isalpha() for c in s)] 
print(list2)

#4 Split a string on hyphens
str1 = "Emma-is-a-data-scientist"
words = str1.split("-")
for word in words:
    print(word)