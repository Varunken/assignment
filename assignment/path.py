"""
Write a function that accesses a value in a nested dictionary given a list of keys representing the 
path to the value.

Input Dictionary: {'a': {'b': {'c': 1}}}, Keys: ['a', 'b', 'c']
Output: 1
"""
dict1 = {'a': {'b': {'c': 1}}}
for x,y in dict1.items():
    if isinstance(y,dict):
        for key,value in y.items():
            if isinstance(value,dict):
                for i in value:
                    print(value.get(i))
            else:
                print(value)
    else:
        print(y)    