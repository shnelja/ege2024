file = [int(x) for x in open('11481.txt')]

max8 = -1 * 10**34
for i in file:
    if int(str(abs(i))[0]) == 8 and i > max8:
        max8 = i

count = 0
sums = []
for j in range(len(file) - 2):
    fst, snd, trd = file[j], file[j + 1], file[j + 2]

    count6 = 0
    for p in fst, snd, trd:
        if int(str(abs(p))[0]) == 6:
            count6 += 1

    if count6 <= 1 and fst + snd + trd >= max8:
        count += 1
        sums.append(fst + snd + trd)

print(count, min(sums))
