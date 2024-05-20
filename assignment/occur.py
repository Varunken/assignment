"""
Given a string, count the number of occurrences of each unique character.

Input: string = "hello world"
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
"""
def occur_char(arg):
    dic = dict()
    for i in arg:
        dic[i] = arg.count(i)
    return dic
string = "hello world"
new_dict = occur_char(string)
print(f"The count of number of occurrences of each unique charcter in string {string} is \n {new_dict}")