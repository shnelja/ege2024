def f(x, end):
    if x == end:
        return 1
    elif x < end:
        return 0
    else:
        return f(x - 3, end) + f(x - 1, end)
    
print(f(34, 25) * f(25, 22) * f(22, 18))