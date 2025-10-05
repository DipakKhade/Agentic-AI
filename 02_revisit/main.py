
#### immutable data types 
# numbers are immutable
n = 1
print(f"mameory location of n ---- {id(n)}")

n = 3
print(f"mameory location of n ---- {id(n)}")   #id will change will shows us that python is moving the pointer to different meomery location since numbers are immutable


#### mutable data types
# sets are mutable
s = set("dipak")
print(f"memory location of s ---- {id(s)}")

s.add("gaurav")
print(f"memory location of s ---- {id(s)}")  #id will not change since python can mutate the set at the same meomery location




