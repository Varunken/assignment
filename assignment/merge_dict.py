"""
Implement a function that takes two dictionaries as input and merges them into a single dictionary, 
with values from the second dictionary overwriting values from the first if keys overlap.

Input: {'a': 1, 'b': 2}, {'b': 3, 'c': 4}
Output: {'a': 1, 'b': 3, 'c': 4}
"""
first_dict = {'a': 1, 'b': 2} 
second_dict = {'b': 3, 'c': 4}
def merge_dict(arg1,arg2):
    dict1 = arg1
    dict2 = arg2
    for key,value in dict2.items():
        dict1.update({key:value})
    return dict1
merged_dict = merge_dict(first_dict,second_dict)
print(f"Merged dict of {first_dict} and {second_dict} is {merged_dict}")
