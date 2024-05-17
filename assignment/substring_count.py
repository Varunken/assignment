"""
Write a function that takes a string and a substring as input and returns the count of 
occurrences of the substring in the string.

Input String: "hello world", Substring: "lo"
Output: 1
"""
def substr_count(string,substr):
    new_string = str(string)
    substring = str(substr)
    pos = 0
    count = new_string.count(substring)
    return count
str1 = input("Enter a string \t")
substr1 = input("Enter the substring \t")
result = substr_count(str1,substr1)
print(f"Count of occurrences of {substr1} in the {str1} is {result}")        