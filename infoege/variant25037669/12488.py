def f(n):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r += '0'
        r = r.replace(r[:2], '11', 1)
    else:
        r += '1'
        r = r.replace(r[:2], '10', 1)
    return int(r, 2)


answer = -1
for x in range(50):
    if f(x) > answer:
        answer = f(x)
print(answer)
