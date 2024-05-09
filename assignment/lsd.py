lis=[1, 2,'Varun','Virat Kohli','Anupama',(3.5,4.5,5.7,6),{21,23,22,22,21,23,27},{'Name': 'Varun', 'a': 'A', 'b': 'B'},True,False]
for i in lis:
    if isinstance(i,list)or isinstance(i,str) or isinstance(i,set) or isinstance(i,tuple):
        print('\t\t\t\t',i)
        for j in i:
            print(j)
        print('\n')
    elif isinstance(i,dict):
        print('\t\t\t\t',i)
        for x,y in i.items():
            print(x,y)
    else:
        print(i)

