def f(x, end):
    if x == end:
        return 1
    elif x < end:
        return 0
    else:
        return f(x - 3, end) + f(x // 2, end)
    
print(f(28, 3))