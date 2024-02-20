def simple(n):
    outCount = 0
    for i in range(1, n + 1):
        if n % i == 0:
            outCount += 1
    if outCount == 2:
        return True
    else:
        return False


file = [int(x) for x in open('10771.txt')]

count = 0
sums = []
for j in range(len(file) - 2):
    fst, snd, trd = file[j], file[j + 1], file[j + 2]

    count3 = 0
    for p in fst, snd, trd:
        if str(p).count('3') >= 1:
            count3 += 1

    if count3 == 3 and simple(fst + snd + trd):
        count += 1
        sums.append(fst + snd + trd)

print(count, min(sums))
