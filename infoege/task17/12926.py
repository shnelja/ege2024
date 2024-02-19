file = [int(x) for x in open('12926.txt')]

A = -1 * 10 ** 34
for i in range(len(file) - 3):
    fst, snd, trd, fth = file[i], file[i + 1], file[i + 2], file[i + 3]

    if fst + snd + trd + fth > A and len({abs(fst) % 10, abs(snd) % 10, abs(trd) % 10, abs(fth) % 10}) == 1:
        A = fst + snd + trd + fth

maxTwo = -1 * 10 ** 34
for k in file:
    if len(str(abs(k))) == 2 and k > maxTwo:
        maxTwo = k

count = 0
sums = []
for j in range(len(file) - 4):
    fst, snd, trd, fth, five = file[j], file[j + 1], file[j + 2], file[j + 3], file[j + 4]

    countA = 0
    for p in fst, snd, trd, fth, five:
        if p < A:
            countA += 1

    if countA == 1:
        if abs(fst + snd + trd + fth + five) % maxTwo == 0:
            count += 1
            sums.append(fst + snd + trd + fth + five)

print(count, min(sums))
# 24 -22671
