def f(x, end):
    if x == end:
        return 1
    elif x < end or x == 32:
        return 0
    else:
        return f(x - 1, end) + f(x - 5, end)
    
print(f(42, 23) * f(23, 22) * f(22, 9))