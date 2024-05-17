"""
Implement a function that takes a dictionary as input and returns a dictionary sorted by its values 
in ascending order.

Input: {'a': 3, 'b': 1, 'c': 2}
Output: {'b': 1, 'c': 2, 'a': 3}
"""
def sort1(arg):
    dic = arg
    key = list(dic.keys())
    value = list(dic.values())
    value.sort()
    i = -1
    sorted_dict = dict()
    while sorted_dict.__len__() < dic.__len__():
        i+=1
        for x in dic.keys():
            if dic.get(x) == value[i]:
                sorted_dict[x] = value[i]
                #print(sorted_dict)
    return sorted_dict        
dict1 = {'a': 3, 'b': 11, 'c': 12,'d': 4}
sort_dict = sort1(dict1)
print(f"After sorting the dictionary {dict1} is {sort_dict}")