file = [int(x) for x in open('12471.txt')]

max3 = 0
for i in file:
    if int(str(i)[-2:]) == 13 and i > max3:
        max3 = i

count = 0
result = 0
for j in range(len(file) - 2):
    fst, snd, trd = file[j], file[j + 1], file[j + 2]

    countEven = 0
    for k in fst, snd, trd:
        if k % 2 == 0:
            countEven += 1

    countTwo = 0
    for p in fst, snd, trd:
        if len(str(p)) == 2:
            countTwo += 1

    if countEven == 3 or countTwo >= 1:
        if fst + snd + trd <= max3:
            count += 1
            result += fst + snd + trd

print(count, (result / count) // 1)
