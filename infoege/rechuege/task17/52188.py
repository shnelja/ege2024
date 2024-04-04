file = [int(x) for x in open('52188.txt')]

min3s = []
for j in file:
    if abs(j) % 10 == 3:
        min3s.append(j)
squareMin3 = min(min3s)**2

count = 0
squareSums = []
for i in range(len(file) - 1):
    fst, snd = file[i], file[i + 1]

    if abs(min(fst, snd)) % 10 == 3 and (fst**2 + snd**2) < squareMin3:
        count += 1
        squareSums.append(fst**2 + snd**2)

print(count, max(squareSums))
