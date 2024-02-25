file = [int(x) for x in open('4368.txt')]

max37 = 0
for i in file:
    if i % 37 == 0:
        max37 = max(max37, i)

count = 0
sums = []
for j in range(len(file) - 1):
    fst, snd = file[j], file[j + 1]

    count37 = 0
    for p in fst, snd:
        if p % max37 == 0:
            count37 += 1

    if count37 >= 1 and (fst + snd) % max37 > 30:
        count += 1
        sums.append(fst + snd)

print(count, min(sums))
