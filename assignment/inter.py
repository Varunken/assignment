"""
Implement a function that takes two dictionaries as input and returns a new dictionary containing 
only the keys that are common to both dictionaries, along with their corresponding values.

Input: {'a': 1, 'b': 2}, {'b': 3, 'c': 4}
Output: {'b': 2}
"""
def intersection(arg1,arg2):
    dict1 = dict(arg1)
    dict2 = dict(arg2)
    interd = dict()
    interd_key = list()
    interd_value = list()
    for i in dict1.keys():
        for j in dict2.keys():
            if i == j:
                interd_key.append(i)
                interd_value.append([dict1.get(i),dict2.get(j)]) 
    for i in range(len(interd_key)):
        interd[interd_key[i]] = interd_value[i]
    return interd
first = {'a': 1, 'b': 2, 'c': 5} 
second = {'b': 3, 'c': 4,'e':6} 
inter = intersection(first,second)
print(f"The intersection of {first} and {second} is {inter}")   