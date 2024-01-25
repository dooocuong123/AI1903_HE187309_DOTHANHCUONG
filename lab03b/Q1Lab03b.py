def is_anagram(str1, str2):
    # Remove white space and punctuation
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()

    # Check if the length of the strings are equal
    if len(str1) != len(str2):
        return False

    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)

# Test
str1 = "parliament"
str2 = "partial men"
if is_anagram(str1, str2):
    print(f"{str1} and {str2} are anagrams!")
else:
    print(f"{str1} and {str2} are not anagrams.")
