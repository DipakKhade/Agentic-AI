
def generateFoo():
    yield 1
    yield 2
    yield 3

result = generateFoo()
print(next(result))
print(next(result))
print(next(result))
