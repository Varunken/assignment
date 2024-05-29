
def generate():
    yield 0
    yield 1
    yield 2
    yield 3
    yield 4
    yield "Varun"
c = generate()
next(c)

try:
    c.__next__()
    print(list(c))
    next(c)
    #next(c)
    #next(c)
except:
    print("OverflowError")
finally:
    print(list(c))