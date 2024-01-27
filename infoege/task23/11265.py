def f(x, end):
    if x == end:
        return 1
    elif x < end:
        return 0
    else:
        return f(x - 4, end) + f(x // 3, end)
    
print(f(36, 2))