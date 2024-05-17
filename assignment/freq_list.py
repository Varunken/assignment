"""
Create a function that takes a list of numbers as input and returns a dictionary containing the 
frequency of each unique number in the list.

Input: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
Output: {1: 1, 2: 2, 3: 3, 4: 4}
"""
def freq(arg):
    num = list(arg)
    dic = dict()
    for i in num:
        dic[i] = num.count(i)
    return dic
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
uniq = freq(numbers)
print(f"Dictionary containing the frequency of each unique number in {numbers} is {uniq}")