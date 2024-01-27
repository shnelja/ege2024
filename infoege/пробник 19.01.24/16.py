from sys import setrecursionlimit

setrecursionlimit(5400)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n + f(n - 1)

count = 0
for i in range(1, 101):
    if (f(2023) // f(i)) % 2 == 0:
        count += 1

print(count)