"""
Write a function that takes a dictionary of student names as keys and their corresponding 
grades as values, and returns a new dictionary where the grades are replaced with their 
letter equivalents ('A', 'B', 'C', 'D', 'F').

Input: {'Dilip': 85, 'Poornima': 92, 'Kushal': 78}
Output: {'Dilip': 'B', 'Poornima': 'A', 'Kushal': 'C'}
"""
def grade(args):
    grd = dict(args)
    key = list(args.keys())
    value = list(args.values())
    for i in key:
        if grd.get(i) in range(90,101):
            grd[i]='A'
        elif grd.get(i) in range(81,90):
            grd[i]='B'
        elif grd.get(i) in range(71,80):
            grd[i]='C'
        elif grd.get(i) in range(51,70):
            grd[i]='D'
        else:
            grd[i]='Fail'
    return grd
dict1 = {'Dilip': 85, 'Poornima': 92, 'Kushal': 78,'Vinay': 65}
new_dic = grade(dict1)
print(f"New dictionary where the grades are replaced with letter equivalents {dict1} is {new_dic}")