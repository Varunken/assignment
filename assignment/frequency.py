"""
Word Frequency
Create a function that takes a list of words as input and returns a dictionary containing the 
frequency of each word in the list.

Input: ["apple", "banana", "apple", "orange", "banana"]
Output: {'apple': 2, 'banana': 2, 'orange': 1}
"""
fruits = ["apple", "banana", "apple", "orange", "banana"]
new_dict = dict()
for i in fruits:
    new_dict[i]=fruits.count(i)
print(new_dict)