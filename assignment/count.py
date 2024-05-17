"""
Write a function that takes a string as input and returns a dictionary containing 
the count of each vowel in the string.

Input: "hello world"
Output: {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
"""
def counts(args):
    vowel = {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
    string = args.lower()
    for i in vowel.keys():
        vowel[i] = string.count(i)
        #vowel.update({i:string.count(i)})
    return vowel
str1 = input("Enter a string\t")
var = counts(str1)
print(var)
