file = [int(x) for x in open('51986.txt')]

min5s = []
for j in file:
    if j % 10 == 5:
        min5s.append(j)
min5 = min(min5s)

count = 0
squareSums = []
for i in range(len(file) - 1):
    fst, snd = file[i], file[i + 1]

    if min(fst, snd) % 10 == 5 and (fst**2 + snd**2) < min5**2:
        count += 1
        squareSums.append(fst**2 + snd**2)

print(count, max(squareSums))
