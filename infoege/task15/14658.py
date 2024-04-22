def f(n, m):
    if abs(n) % abs(m) == 0:
        return True
    else:
        return False


for a in range(1, 5001):
    k = 0
    for x in range(1, 5001):
        if (f(x, 12) <= (not (f(x, 42)))) or ((x + a) >= 4096):
            k += 1
    if k == 5000:
        print(a)
        break
