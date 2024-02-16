def algorithm(n):
    r = bin(n)[2:]
    r += bin(n % 4)[2:]
    return int(r, 2)


available = [algorithm(x) for x in range(1, 10000)]

counts = []
for j in range(1000):
    count = 0
    for i in range(j + 1, j + 50):
        if i not in available:
            continue
        else:
            count += 1
    counts.append(count)

print(max(counts))
