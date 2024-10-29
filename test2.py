x=10
def foo():
    if x is None:
        print('none')
    else:
        print(x)
        x = 20

foo()