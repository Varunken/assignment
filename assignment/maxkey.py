"""
Write a function that finds the key with the maximum  and minimum value in a dictionary.

Input: {'a': 10, 'b': 20, 'c': 15}
Output: 'b'
"""
def minvalue(arg):
    str = ''
    value = list(arg.values())
    value.sort()
    for key in arg.keys():
        if arg.get(key) == value[0]:
            str = key
    return str

def maxvalue(arg):
    str = ''
    value = list(arg.values())
    value.sort()
    for key in arg.keys():
        if arg.get(key) == value[-1]:
            str = key
    return str

dic = {'a': 10, 'b': 20, 'c': 15}
max = maxvalue(dic)
min = minvalue(dic)
print(f"The key with the max value in the dictionary {dic} is {max}")
print(f"The key with the min value in the dictionary {dic} is {min}")