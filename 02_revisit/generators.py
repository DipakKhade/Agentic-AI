
def generateFoo():
    yield 1
    yield 2
    yield 3

result = generateFoo()
print(next(result))
print(next(result))
print(next(result))


def say_name():
    name = yield
    while True:
        print(f"your name is : {name}")
        name = yield

print_name = say_name()
next(print_name)
print_name.send('Dipak')
print_name.send('Gaurav')


def generateFaa():
    yield 4
    yield 5

def allFooFa():
    yield from generateFoo()
    yield from generateFaa()

for x in allFooFa():
    print(x)