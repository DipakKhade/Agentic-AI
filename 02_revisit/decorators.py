
def my_decorator(fn):
    def wrapper():
        print('defore calling fn') 
        fn()
        print('after calling fn')
    return wrapper

def Foo():
    print('you have called Foo fn')

# dec = my_decorator(Foo)
# dec()

@my_decorator
def Faa():
    print('you have called Faa fn')

Faa()