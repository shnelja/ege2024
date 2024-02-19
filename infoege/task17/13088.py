file = [int(x) for x in open('13088.txt')]

max17 = 0
count = 0
maxSum = 0
for i in file:
    if str(i)[-2:] == '17' and i > max17:
        max17 = i

for k in range(len(file) - 2):
    fst, snd, trd = file[k], file[k + 1], file[k + 2]

    count4 = 0
    for p in fst, snd, trd:
        if len(str(p)) == 4:
            count4 += 1

    count5 = 0
    for j in fst, snd, trd:
        if j % 5 == 0:
            count5 += 1

    if count4 == 2:
        if count5 >= 1:
            if fst + snd + trd > max17:
                count += 1
                if fst + snd + trd > maxSum:
                    maxSum = fst + snd + trd

print(count, maxSum)
# 21 114132
