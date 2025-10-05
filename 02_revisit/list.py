
l = ['a', 'b', 'c']
l.append('d')

pop_return_value = l.pop(0)
print(pop_return_value)

l2 = ['d', 'e', 'f']
l.extend(l2)

l.insert(0, 'my name is dipak')

l.reverse()

def asd(a):
    return a+'1'

m = list(map(asd, l))

print(m)