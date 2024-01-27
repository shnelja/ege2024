def f(x, end):
    if x == end:
        return 1
    elif x > end:
        return 0
    else:
        return f(x + 2, end) + f(x + 3, end)
    
print(f(8, 28) * f(28, 31) * f(31, 43))