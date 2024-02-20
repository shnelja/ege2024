file = [int(x) for x in open('11703.txt')]

max18 = -1 * 10**34
for i in file:
    if int(str(i)[-2:]) == 18 and i > max18:
        max18 = i

count = 0
maxMult = -1 * 10**34
for j in range(len(file) - 2):
    fst, snd, trd = file[j], file[j + 1], file[j + 2]

    count5 = 0
    for p in fst, snd, trd:
        if len(str(abs(p))) == 5:
            count5 += 1

    if count5 >= 1:
        if abs(fst * snd * trd) % abs(max18) == 0:
            count += 1
            if fst * snd * trd > maxMult:
                maxMult = fst * snd * trd

print(count, maxMult)
