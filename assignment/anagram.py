"""
Create a function that takes two strings as input and returns True if they are anagrams, False otherwise.

Input: "listen", "silent"
Output: True
"""
def anagram(args1,args2):
    str1 = args1
    str2 = args2
    flag = False
    if sorted(str1) == sorted(str2):
        flag = True
    return flag

string1 = input("Enter a string\t")
string2 = input("Enter a string\t")
if anagram(string1,string2) == True:
    print(f"the strings{string1} and {string2} are anagrams")
else:
    print(f"the strings{string1} and {string2} are not anagrams")
