#Assignment - 2
"""
1. Take user input python program reverse a string using for loop
Sample Input:
name = "Ravi Kumar"
Expected Output:
kamuK ivaR
"""
name =input("Enter a string")
rev=""
j=len(name)
for i in range(0,j):
    rev+=name[j-1]
    j-=1
print(f"After reversing the string {name} is {rev}")
"""
2. Take user input change the values in a list. We want to change value 10 to "changed" using for loop
Sample Input:
list1 = [2,5,10,37,20,10,6,10,55,10]
Expected Output:
[2,5,"changed",37,20,"changed",16,"changed",55,"changed"]
"""
#list1 = [2,5,10,37,20,10,6,10,55,10]
list1=list()
num=int(input("Enter the size of list"))
for i in range(num):
    list1.append(int(input(f"Enter the {i+1} elemnets of list")))
print("original list ",list1)
value=int(input("enter any value from above list"))
#for i in range(list1.count(10)):
for i in range(list1.count(value)):
    list1.__setitem__(list1.index(10),"changed")
print(list1)

"""
3. Take user input follow the below steps
Sample Input:
Step 1:
list1 = [1,3,5,2,22,24,5,6,45,76,98,6]
Step 2:
Devide the even and odd numbers in separate different list
Step 3:
Sum the even numbers and odd numbers
Step 4:
print which value is big
Expected Ouput:
even = [ADD EVEN NUMBERS]
odd = [ADD ODD NUMBERS]
sum the even list(foe example even list total is 48)
sum the odd list(for example odd list total is 69)
print big value like 69
"""
list1 = [1,3,5,2,22,24,5,6,45,76,98,6]
odd_list=list()
even_list=list()
odd=0
even=0
for i in list1:
    if i%2==0:
        even_list.append(i)
        #even+=i
    else:
        odd_list.append(i)
        #odd+=i
for i in odd_list:
    odd+=i
for i in even_list:
    even+=i
print("Sum of even list",even)
print("Sum of odd list",odd)
if odd<even:
    print("Big value is",even)
else:
    print("Big value is",odd)



        
"""

4. Write a python program find the sum of list inside the dictionary without using "sum" function
Sample input:
d = {"list1":[1,2,3,4,5],"names":"sravan","num":101}
Expected Output:
Ans is : 15
"""
d = {"list1":[1,2,3,4,5],"names":"sravan","num":101}
lis=d.get("list1")
total=0
for i in lis:
    total+=i
print(f"the sum of {lis} is {total}")


"""
5. Write a python program to take a string and find the every character lowercase or uppercase print lower characters only
Sample Input:
name = "KArtHik"
Expected Ouput:
rtik
"""
name=input("Enter a string")
lower=""
upper=""
for i in name:
    if i.islower():
        lower+=i
    else:
        upper+=i
print(f"Lowercase letters of string {name} is {lower}")
"""

6. Take a user input string print the every character double
Sample Input:
name = "karthik"
Expected Output:
kk
aa
rr
tt
hh
ii
kk
"""
name=input("Enter a string")
for i in name:
    print(f"{i}{i}")
"""
7. Write a python program count the even numbers and odd numbers in list
Sample Input:
list1 = [1,2,3,4,5,6,7,8,9,10]
Expected Output:
even_numbers 5
odd numbers 5
"""
list1 = [1,2,3,4,5,6,7,8,9,10]
odd=0
even=0
print(list1)
for i in list1:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Odd numbers",odd)
print("Even numbers",even)
"""
8. Take the user input string devide the numbers and alphabets
Sample Input:
str_and_num = "kd3ab5gf12rt33"
Expected Output:
string = kdabgfrt
numbers = 351233
"""
str_and_num=input("Enter a string of combination of numbers and alphabets")
string=str()
numbers=str()
for i in range(len(str_and_num)):
    if str_and_num[i].isdigit():
        numbers+=str_and_num[i]
    elif str_and_num[i].isalpha():
        string+=str_and_num[i]
    else:
        pass
print("String of alphabets",string)
print("String of numbers",numbers)
