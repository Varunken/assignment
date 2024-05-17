"""
Implement a function that takes a dictionary as input and returns a new dictionary where the 
keys and values are inverted.

Input: {'a': 1, 'b': 2, 'c': 3}
Output: {1: 'a', 2: 'b', 3: 'c'}
"""
def invert(args):
    dis = args
    key = list(dis.values())
    value = list(dis.keys())
    inverted_dict = dict()
    for i in range(len(key)):
        inverted_dict.update({key[i]:value[i]})
    return inverted_dict
dic = {'a': 1, 'b': 2, 'c': 3}
inverted_dic = invert(dic)
print(f"after inverting {dic} is {inverted_dic}")

"""
Create a function that takes a dictionary as input and returns a list of unique values in the dictionary.

Input: {'a': 1, 'b': 2, 'c': 1, 'd': 3}
Output: [1, 2, 3]
"""
def unique_value(arg):
    values = tuple(arg.values())
    value = list(values)
    return value
print(f"Unique values in the dictionary {dic} is {unique_value(dic)}")