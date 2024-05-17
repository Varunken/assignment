"""
Create a function that takes a dictionary where keys are binary strings and values 
are their corresponding decimal equivalents, and returns a new dictionary where keys 
are decimal strings and values are their corresponding binary equivalents.

Input: {'10': 2, '11': 3}
Output: {'2': '10', '3': '11'}
"""
def interchange(arg):
    dic = dict(arg)
    keys = list(dic.values())
    values = list(dic.keys())
    n_dic = dict()
    for i in range(len(keys)):
        n_dic[str(keys[i])] = int(values[i])
    return n_dic
binary = {'10': 2, '11': 3}
new_dic = interchange(binary)
print(f"After interchanging the type {binary} is {new_dic}")