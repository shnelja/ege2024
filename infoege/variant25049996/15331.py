from sys import setrecursionlimit
setrecursionlimit(2500)


def f(n):
    if n <= 7:
        return 1
    else:
        return n + 2 + f(n - 1)


print(f(2024) - f(2020))
