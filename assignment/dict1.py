"""
Write a function that takes a string as input and returns a dictionary containing 
the count of each character in the string.

   Input: "hello"
   Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""
string = input("Enter a string")
new_dict = dict()
for i in string:
    new_dict[i]=string.count(i)
print(new_dict)