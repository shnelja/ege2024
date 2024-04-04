file = [int(x) for x in open('37354.txt')]

count = 0
sums = []
for j in range(len(file) - 1):
    for i in range(j + 1, len(file)):
        fst, snd = file[j], file[i]

        if (fst + snd) % 2 != 0 and (fst * snd) % 5 == 0:
            count += 1
            sums.append(fst + snd)

print(count, max(sums))
