"""
Given a sentence, find the frequency of each word.

Input: sentence = "the quick brown fox jumps over the lazy dog"
Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
"""
def freq_count(arg):
    dic = dict()
    string = arg
    substring = ""
    for i in string:
        substring+=i
        if i.isspace():
            dic[substring] = string.count(substring)
            substring = ""
    else:
        dic[substring] = string.count(substring)
    return dic
sentence = "the quick brown fox jumps over the lazy dog"
#sentence = input("Enter a sentence\t")
new_dict = freq_count(sentence)
print(f"Frequency of each word    {new_dict}")
