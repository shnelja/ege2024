def f(x, end):
    if x == end:
        return 1
    elif x < end:
        return 0
    else:
        return f(x - 3, end) + f(x - 1, end) + f(x // 2, end)
    
print(f(39, 19) * f(19, 16) * f(16, 7))