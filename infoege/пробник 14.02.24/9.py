k = 0
for i in open('files/09.csv'):
    x = list(map(int, i.split(';')))
    p1 = any(x.count(c) > 1 for c in x)
    p2 = x.count(max(x)) == 1
    p3 = sum([c for c in x if x.count(c) > 1]) > max(x)
    if p1 and p2 and p3:
        k += 1

print(k)
