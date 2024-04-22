file = open('files/9_15321.txt')
count = 0
for line in file:
    a = sorted(int(x) for x in line.split())
    if a[3] < sum(a[0:2]):
        if a[3] + a[0] == a[1] + a[2]:
            count += 1
print(count)
