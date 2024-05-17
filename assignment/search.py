"""
Implement a function that takes a dictionary representing a phonebook and a name to search for, 
and returns the phone number associated with that name.

Input Phonebook: {'Dilip': '123-456', 'Sudeeksha': '789-101'}
Name to search: 'Dilip'
Output: '123-456
"""
def search(args,item):
    pbk = dict(args)
    element = item
    result = pbk.get(element)
    return result
call_log = {'Dilip': '123-456', 'Sudeeksha': '789-101'}
name = input("Enter a name to search ")
number = search(call_log,name)
if number == None:
    print(f"{name} is not present in phonebook")
else:
    print(f"Phone number associated with the {name} is {number}")   
    