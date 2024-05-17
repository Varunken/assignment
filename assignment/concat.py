"""
Implement a function that takes two dictionaries as input and returns a new dictionary
 containing all the key-value pairs from both dictionaries.

Input: {'a': 1, 'b': 2}, {'c': 3, 'd': 4}
Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
"""
def concat(arg1,arg2):
    first = dict(arg1)
    second = dict(arg2)
    for key,value in second.items():
        first[key] = value
    return first
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}
new_dict = concat(dict_1,dict_2)
print(f"Concatenation of {dict_1} and {dict_2} is {new_dict}")