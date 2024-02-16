from itertools import product

a = '1357'
b = '2468'
count = 0
for x in product(a, b, a, b, a, b, a, b, a, b, a):
    c = ''.join(x)
    if all(c.count(s) <= 4 for s in c):
        count += 1

print(count * 2)
