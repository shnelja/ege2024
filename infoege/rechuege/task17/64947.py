file = [int(x) for x in open('64947.txt')]

max832s = []
for j in file:
    if j % 1000 == 832:
        max832s.append(j)
max832 = max(max832s)

count = 0
sums = []
for i in range(len(file) - 2):
    fst, snd, trd = file[i], file[i + 1], file[i + 2]

    count4 = count3 = count5 = 0
    for x in fst, snd, trd:
        if len(str(x)) == 4:
            count4 += 1
        if x % 3 == 0:
            count3 += 1
        if x % 5 == 0:
            count5 += 1

    if 0 < count4 < 3:
        if count5 > count3:
            if (fst + snd + trd) > max832:
                count += 1
                sums.append(fst + snd + trd)

print(count, max(sums))
