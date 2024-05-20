"""
Check if a key exists in a dictionary.

Input: my_dict = {'a': 1, 'b': 2, 'c': 3}, key = 'b'
Output: True
"""
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
num = 0
while True:
    print("\n\nDictionary operations \n 1.Dictionary keys\n2.Dictionary values\n3.If Key exist or not \n4.If value exist or not \n 5.sum of values \n6.Value update \n7.Element deletion using key \n8.quit  ")
    opt = int(input("Select a dictionary operations \t"))
    if opt == 1:
        print(f"Keys of dictionaries\t {my_dict.keys()}")
    elif opt == 2:
        print(f"Values of dictionaries\t {my_dict.values()}")
    elif opt == 3:
        key = input("Enter a key ")
        if key in my_dict.keys():
            print("Key exists")
        else:
            print(f"{key} does not exist in {my_dict}")
    elif opt == 4:
        value = int(input("Enter a value "))
        if value in my_dict.values():
            print("Value exists")
        else:
            print(f"{value} does not exist in {my_dict}")
    elif opt == 5:
        total = 0
        for i in my_dict.values():
            total+=i
        print("Sum of values is  ",total)
    elif opt == 6:
        key = input("Enter a key ")
        value = input("Enter a value to update ")
        my_dict.update({key:value})
        print(f"After updation of key{key} with value {value} \t {my_dict}")
    elif opt == 7:
        key = input("Enter a key ")
        my_dict.pop(key)
        print(f"After deletion of {key} \t {my_dict}")
    elif opt == 8:
        break