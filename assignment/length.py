"""
Calculate the length of a dictionary.

Input: my_dict = {'a': 1, 'b': 2, 'c': 3, }
Output: 3
"""
my_dict = {'a': 1, 'b': 2, 'c': 3,'d': 4}
length = 0
for i in my_dict:
    length+=1
print(f"Length of dictionary {my_dict} is {length}")