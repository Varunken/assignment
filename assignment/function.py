def arms(arg):
    order=len(str(arg))
    num=arg
    sum=0
    total=0
    while num>0:
        sum=num%10
        sum=sum**order
        total+=sum
        num//=10
    if total==arg:
        print(arg)     
for i in range(1,10000):
    arms(i)