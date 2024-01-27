def f(x, end):
    if x == end:
        return 1
    elif x < end or x == 11:
        return 0
    else:
        return f(x - 1, end) + f(x - 2, end) + f(x // 3, end)
    
print(f(30, 8))