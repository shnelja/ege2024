file = [int(x) for x in open('10100.txt')]

max13 = -1 * 10**34
for i in file:
    if i > max13 and int(str(i)[-2:]) == 13:
        max13 = i

count = 0
maxSum = -1 * 10**34
for j in range(len(file) - 2):
    fst, snd, trd = file[j], file[j + 1], file[j + 2]

    count3 = 0
    for p in fst, snd, trd:
        if len(str(abs(p))) == 3:
            count3 += 1

    if count3 == 2 and fst + snd + trd <= max13:
        count += 1
        if fst + snd + trd > maxSum:
            maxSum = fst + snd + trd

print(count, maxSum)
