from sys import setrecursionlimit
setrecursionlimit(16000)


def f(n):
    if n < 52:
        return n
    else:
        return 3 * f(n - 2) - n


print(f(15127) // f(15099))
