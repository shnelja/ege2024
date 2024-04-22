def f(x, end):
    if x == end:
        return 1
    elif x > end:
        return 0
    else:
        return f(x + 1, end) + f(x * 2, end)


print(f(4, 8)*f(8, 10)*f(10, 15))
