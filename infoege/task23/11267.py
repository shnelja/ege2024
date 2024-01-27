def f(x, end):
    if x == end:
        return 1
    elif x < end or x == 35:
        return 0
    else:
        return f(x // 3, end) + f(x - 2, end) + f(x - 5, end)
    
print(f(41, 37) * f(37, 8))