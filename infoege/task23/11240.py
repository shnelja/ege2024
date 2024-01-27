def f(x, end, c):
    if x == end and 'bb' not in c:
        return 1
    elif x > end:
        return 0
    else:
        return f(x + 2, end, c + 'a') + f(x ** 2, end, c + 'b') + f(x * 3, end, c + 'c')

print(f(2, 64, ''))