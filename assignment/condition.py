"""
Implement a function that takes a dictionary and a condition function as input, 
and returns a new dictionary containing only the key-value pairs that satisfy the condition function.

Input: {'a': 1, 'b': 2, 'c': 3, 'd': 4}, Condition: lambda x: x % 2 == 0
Output: {'b': 2, 'd': 4}
"""
def condition(arg,cond):
    dic = dict(arg)
    nest = cond
    new_dic = dict()
    new_value = list()
    value = list(dic.values())
    for i in value:
         if nest(i) == True:
             new_value.append(i)
    for x in dic.keys():
        for y in new_value:
            if dic.get(x) == y:
                new_dic[x] = y
    return new_dic
 
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
cond = lambda i : i % 2 == 0
new_dict = condition(my_dict,cond)
print(new_dict)
