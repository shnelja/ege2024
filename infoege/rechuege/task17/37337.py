file = [int(x) for x in open('37337.txt')]

d, p = 160, 7

count = 0
sums = []
for j in range(len(file) - 1):
    for i in range(j + 1, len(file)):
        fst, snd = file[j], file[i]

        countP = 0
        for x in fst, snd:
            if x % p == 0:
                countP += 1

        if countP >= 1 and fst % d != snd % d:
            count += 1
            sums.append(fst + snd)

print(count, max(sums))
