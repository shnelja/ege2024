def f(x, end):
    if x == end:
        return 1
    elif x > end:
        return 0
    else:
        return f(x + 3, end) + f(x + 4, end) + f(x + 2, end)
    
print(f(6, 32) * f(32, 35) * f(35, 44))