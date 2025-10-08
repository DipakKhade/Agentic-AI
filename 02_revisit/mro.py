# Method Resolution Order

class A:
    id=1

class B:
    id=2

class C:
    id=3

class D(C, B, A):
    def __init__(self):
        pass

instance = D()
print(instance.id)

print(D.__mro__)