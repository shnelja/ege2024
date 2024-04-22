def f(n, m):
    if abs(n) % abs(m) == 0:
        return True
    else:
        return False


for a in range(1, 2501):
    k = 0
    for x in range(1, 2501):
        if (((not(f(x, 17))) or (not(f(x, 12)))) <= (not(f(x, a)))):
            k += 1
    if k == 2500:
        print(a)
        break
