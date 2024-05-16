#Smallest number in a list
list1 = [5,3,99,5,3,8,3,2,1,7,88,76,54,1]
print("list\t\t",list1)
list1.sort()
print("the smallest number in the list is\t",list1[0])


#Largest number in a list
#list1 = [5,3,99,5,3,8,3,2,1,7,88,76,54,1]
print("the largest number in the list is\t",list1[-1])


#Second smallest number in a list
for i in range(list1.count(list1[0])):
    list1.remove(list1[0])
print("the second smallest number in the list is\t",list1[0])

#Second largest number in a list
for i in range(list1.count(list1[-1])):
    list1.pop()
print("the second largest number in the list is\t",list1[-1])

"""5. Write a python program follow the below steps don't use new list
Sample Input: 
list1 = [4,8,3,1,15]
step 1:
find smallest value in a list -----> 1
step 2:
find largest value in a list  -------> 15
step 3:
add the values in same list whatever missing numbers in between smallest value and largest value -----> 1 and 15
step 4:
print the list sequential order like [1,2,3,4,5..............]
Expected Output:
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]"""


lis=[4,8,3,1,15]
print("list\n\n",lis)
lis.sort()
print("smallest value in a list",lis[0])
print("largest value in a list",lis[-1])
print([i for i in range(lis[0],(lis[-1])+1)])


"""6. Find the length of string without using len() function
Sample Input:
name = "Chiranjeevi"
Expected Output:
11"""
name = "Chiranjeevi"
length=0
for i in name:
    length+=1
print(f"length of a string {name} is {length}")
"""
7. Take a list with values, take user input integer value, if user input value is there in list multiple that value with each and every value in a list
Sample Input:
values = [3,1,5,7,12,11,8,9,2,3]
Take user input value for example 5. 5 is available in list so multiple 5 value with list values
If user value is not there in a list print the numbr is not there in a list
Expected output:
5 * 3 = 15
5 * 1 = 5
5 * 5 = 25
......
......
"""
values = [3,1,5,7,12,11,8,9,2,3]
print(values)
num=int(input("Enter any value from above list\t"))
if num in values:
    for i in values:
        print(f"\t{num} * {i} = {num*i}")
else:
    print(f"{num} is not there in the list")




"""
8. Write a python program to clear the all values in a list without using clear() method. Use for loop.
Sample Input:
list1  [1,2,3,4,5,6,7]
Ecpected Output:
[] ------> Empty list
"""
lis1=[1,2,3,4,5,6,7]
print(lis1)
for i in range(len(lis1)):
    lis1.pop()
print(lis1)
"""
9. Take two list, that two list should be same length. You can create dictionary first list elements are keys and second list elements are values
Sample Input:
keys = [1,2,3,4,5,6]
values = [100,200,300,400,500,600]
Expected Output:
d = {1:100,2:200,3:300,4:400,5:500,6:600}
"""
keys = [1,2,3,4,5,6]
values = [100,200,300,400,500,600]
d={}
for i in range(len(keys)):
    d.update({keys[i]: values[i]})
print(f"Dictionary using {keys}and{values} is\n{d}")

"""
10. Write a python program print the duplicate elements in a list
Sample Input:
list1 = [1,2,3,4,5,1,5,10,11,35,24,8,10,35]
Expected Output:
1 5 10 35"""
list3 = [1,2,3,4,5,1,5,10,11,35,24,8,10,35]
print(list3)
s1=set()
for i in list3:
    if list3.count(i)>1:
        s1.add(i)
#print(s1)
print("Duplicates elements in the list")
for i in s1:
    print(i)
