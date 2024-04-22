def f(x, end):
    if x == end:
        return 1
    elif x > end or x == 16:
        return 0
    else:
        return f(x + 2, end) + f(x * 3, end) + f(x * 2, end)


print(f(13, 45))