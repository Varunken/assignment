"""
Write a function that finds the key with the maximum value in a dictionary.

Input: {'a': 10, 'b': 20, 'c': 15}
Output: 'b'
"""
def maxvalue(arg):
    str = ''
    value = list(arg.values())
    value.sort()
    for key in arg.keys():
        if arg.get(key) == value[-1]:
            str = key
    return str

dic = {'a': 10, 'b': 20, 'c': 15}
result = maxvalue(dic)
print(f"The key with the max value in the dictionary {dic} is {result}")