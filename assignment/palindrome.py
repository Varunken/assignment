"""
Create a function that takes a string as input and returns True if it is a palindrome, False otherwise.

Input: "racecar"
Output: True
"""
def palindrome(arg):
    rev = ''
    length = len(arg)
    flag = False
    for i in range(length):
        rev+=arg[length-1]
        length+=-1
    if rev == arg:
        flag = True
    return flag
string = input("Enter a string\t")
result = palindrome(string)
print([f"{string} is a palindrome" if result==True else f"{string} is not a palindrome"])
        