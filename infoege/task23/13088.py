def f(x, e, l):
    if x == e:
        return 1
    if x > e + 10:
        return 0
    if l == 'a':
        return f(x * 2, e, 'b') + f(x * 3, e, 'c')
    if l != 'a':
        return f(x - 1, e, 'a') + f(x * 2, e, 'b') + f(x * 3, e, 'c')


print(f(3, 15, ''))