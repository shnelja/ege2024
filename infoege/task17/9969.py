def f(n): return n >= 0 and n ** 0.5 % 1 == 0


a = list(map(int, open('9969.txt')))
m = max(a, key=lambda k: (len(set(str(abs(k)))), k))
b = []

for i in range(len(a) - 2):
    x, y, z = a[i:i + 3]

    d = [
        (y + z) if f(x) else 0,
        (x + z) if f(y) else 0,
        (x + y) if f(z) else 0,
    ]

    if sum(x > 0 for x in d) == 1 and sum(d) >= m:
        b += [x + y + z - sum(d)]

print(len(b), sum(b))
