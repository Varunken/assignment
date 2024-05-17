"""
Given a sentence, calculate the average length of words in it.

Input: sentence = "The quick brown fox jumps over the lazy dog"
Output: 3.857
Explanation: Average length of words = (3 + 5 + 5 + 3 + 5 + 4 + 3 + 4) / 8 = 32 / 8 = 4
"""
#sentence = "The quick brown fox jumps over the lazy dog"
sentence = input("Enter a sentence\t")
space_count = 1
count = 0
for i in sentence:
    count+=1
    if i.isspace():
        space_count+=1
        count-=1
avg = count/space_count
print(f"The average length of string is {avg}")