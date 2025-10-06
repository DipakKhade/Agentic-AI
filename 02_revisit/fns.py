
def foo(**x):
    print(f'inputes are {x}')
    return

foo(a= 1)

def addup(*args):
    return sum(args)

print(addup(2,3,4))


#----------------------------------------
# *args ===> get the inputs as tuple   call--> fn(1,2,3,3,3,4)
# **kwargs ===> get the inputs as dictnory  call--> fn(a=2, b=3)
