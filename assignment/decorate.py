"""def decorator(func):
    def inner(a):
        version = "PD1814F"
        print(version)
        func()
        return inner
#@decorator
def model(a,b):
    name = a
    build_id = b
    print( name,build_id)
out=model("Vivo",1.1)
#print(out())
inp = decorator(model)
inp()"""
def make_pretty(func):
    print("decorated function")
    x = 100
    def inner(x):
        x = 10
        print("I got decorated")
        func(x*x)
    return inner

@make_pretty
def ordinary(x):
    number = x
    print("I am ordinary",number)

ordinary(5)
