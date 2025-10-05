
#list
l = [i for i in range(1,11) if i % 2 == 0]
print(l)

#sets
m = ['a', 'a', 'b']
s = {x for x in m}
print(s)

#dictionary

f = ['Dipak', 'Gaurav']
d = {index:x for (index, x) in enumerate(f)}
print(d)