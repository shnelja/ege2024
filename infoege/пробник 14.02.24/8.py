from itertools import product

<<<<<<< HEAD
a = '1357'
b = '2468'
count = 0
for x in product(a, b, a, b, a, b, a, b, a, b, a):
    c = ''.join(x)
    if all(c.count(s) <= 4 for s in c):
        count += 1

print(count * 2)
=======
a = '2468'
b = '1357'
k = 0
for x in product(a, b, a, b, a, b, a, b, a, b, a):
    j = ''.join(x)
    if all(j.count(s) <= 4 for s in j):
        k += 1

print(k*2)
>>>>>>> origin/master
