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


