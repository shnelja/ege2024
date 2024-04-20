def f(n, m):
    if abs(n) % abs(m) == 0:
        return True
    else:
        return False


arr = []
for a in range(1, 1001):
    k = 0
    for x in range(1, 1001):
        if (not (f(x, a))) <= (f(x, 28) <= (not (f(x, 49)))):
            k += 1
        if k == 1000:
            arr.append(a)
print(max(arr))
