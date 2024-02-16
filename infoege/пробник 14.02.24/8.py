from itertools import product

a = '2468'
b = '1357'
k = 0
for x in product(a, b, a, b, a, b, a, b, a, b, a):
    j = ''.join(x)
    if all(j.count(s) <= 4 for s in j):
        k += 1

print(k*2)
