#!/usr/bin/python3

n_max = 1000

l3 = list(range(3,n_max,3))
l5 = list(range(5,n_max,5))

l35 = set().union(l3 + l5) # Faster than set(a+b)
print(sum(l35))
