file = [int(x) for x in open('61397.txt')]

max17s = []
for i in file:
    if i % 100 == 17:
        max17s.append(i)
max17 = max(max17s)

count = 0
sums = []
for j in range(len(file) - 2):
    fst, snd, trd = file[j], file[j + 1], file[j + 2]

    count4 = 0
    count5 = 0
    for x in fst, snd, trd:
        if len(str(x)) == 4:
            count4 += 1
        if x % 5 == 0:
            count5 += 1

    if count4 == 2 and count5 >= 1 and (fst + snd + trd) > max17:
        count += 1
        sums.append(fst + snd + trd)

print(count, max(sums))
