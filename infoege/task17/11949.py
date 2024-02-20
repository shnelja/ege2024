file = [int(x) for x in open('11949.txt')]

max68 = -1 * 10**34
for i in file:
    if int(str(i)[-2:]) == 68 and i > max68:
        max68 = i

count = 0
maxSum = -1 * 10**34
for j in range(len(file) - 3):
    fst, snd, trd, fth = file[j], file[j + 1], file[j + 2], file[j + 3]

    count4 = 0
    for p in fst, snd, trd, fth:
        if len(str(abs(p))) == 2:
            count4 += 1

    if count4 == 1 or count4 == 4:
        if fst + snd + trd + fth >= max68:
            count += 1
            if fst + snd + trd + fth > maxSum:
                maxSum = fst + snd + trd + fth

print(count, maxSum)
