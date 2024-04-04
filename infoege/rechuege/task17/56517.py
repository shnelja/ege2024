file = [int(x) for x in open('56517.txt')]

max3 = -1*10**34
for i in file:
    if abs(i) % 10 == 3:
        max3 = max(max3, i)

count = 0
squareSums = []
for j in range(len(file) - 1):
    fst, snd = file[j], file[j + 1]

    count3 = 0
    for x in fst, snd:
        if abs(x) % 3 == 0:
            count3 += 1

    if abs(fst) % 10 == abs(snd) % 10 and count3 == 1 and (fst**2 + snd**2) <= max3**2:
        count += 1
        squareSums.append(fst**2 + snd**2)

print(count, max(squareSums))
