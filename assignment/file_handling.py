"""content = open('test.txt','r')
#file_content = file_content
#for each in content:
#   print(each)
file_content = content.readline()
print(content.readline())
content.seekable()
content.seek(300)
print(content.readline())
print(file_content)
print(content.tell()) 
#content.write("Varun")
content.close()
print(content.tell())
"""
string = ["Varun","Vegeta","Goku"]
try:
        
    with open("test.txt",'a+') as data:
        """for each in string:
            data.tell()
            data.writelines(each)"""
        print(data.name)
        print(data.write("each"))
        data.seek(123)
        print(f"{data.read(100)}",flush=True)
        content = open('occur.py','r')
        info = content.readlines()
        print(info)
except:
    print("trying to open a file which does not exist in path")
finally:
    content.close
