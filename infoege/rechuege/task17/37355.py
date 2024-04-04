file = [int(x) for x in open('37355.txt')]

count = 0
sums = []
for i in range(len(file) - 1):
    for j in range(i + 1, len(file)):
        fst, snd = file[i], file[j]

        if (fst + snd) % 7 == 0:
            count += 1
            sums.append(fst + snd)

print(count, max(sums))
