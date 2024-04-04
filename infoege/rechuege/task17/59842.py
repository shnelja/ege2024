file = [int(x) for x in open('59842.txt')]

max29s = []
for i in file:
    if abs(i) % 100 == 29:
        max29s.append(i)
max29 = max(max29s)

count = 0
sums = []
for j in range(len(file) - 2):
    fst, snd, trd = file[j], file[j + 1], file[j + 2]

    count5 = 0
    for x in fst, snd, trd:
        if len(str(abs(x))) == 5:
            count5 += 1

    if count5 == 2 and (fst + snd + trd) <= max29:
        count += 1
        sums.append(fst + snd + trd)

print(count, max(sums))
