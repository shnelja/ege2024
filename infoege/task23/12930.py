def f(x, e):
    if x == e:
        return 1
    elif x > e or x == 11 or x == 12:
        return 0
    else:
        return f(x + 1, e) + f(x * 2, e) + f(x ** 2, e)
    
print(f(2, 10) * f(10, 40))