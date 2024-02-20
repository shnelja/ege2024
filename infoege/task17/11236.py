file = [int(x) for x in open('11236.txt')]

fstQuestion = []
for i in file:
    if len(str(abs(i))) == 2:
        fstQuestion.append(i)
square = min(fstQuestion)**2

max41 = -1 * 10**34
for k in file:
    if len(str(abs(k))) == 4 and int(str(k)[-1]) == 1:
        if k > max41:
            max41 = k

count = 0
maxSum = -1 * 10**34
for j in range(len(file) - 2):
    fst, snd, trd = file[j], file[j + 1], file[j + 2]

    countSquare = 0
    for p in fst, snd, trd:
        if p > square:
            countSquare += 1

    if countSquare == 2:
        if (abs(fst) * abs(snd) * abs(trd)) % abs(max41) == 0:
            count += 1
            if abs(fst) + abs(snd) + abs(trd) > maxSum:
                maxSum = abs(fst) + abs(snd) + abs(trd)

print(count, maxSum)
