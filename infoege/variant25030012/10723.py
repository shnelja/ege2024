def f(n, end):
    if n == end:
        return 1
    elif n > end:
        return 0
    else:
        return f(n + 2, end) + f(n ** 2, end) + f(n ** 3, end)


print(f(10, 1000))
