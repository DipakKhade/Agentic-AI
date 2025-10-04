
a = (2)
print(id(a))

a = (2,3)
print(id(a))

#destructure

names = ('gaurav', 'krushna')
(f1, f2) = names

print(f1, f2)

name1, name2 = 'Sonali', 'Dipak'

#swaps
b = 2
c = 3
b, c = c, b
print(f"b {b} and c {c}")

#membership testing
t = ('a', 'b', 'c')
print('c' in t)