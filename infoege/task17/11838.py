file = [int(x) for x in open('11838.txt')]

max50 = -1 * 10**34
for i in file:
    if int(str(i)[-2:]) == 50 and i > max50:
        max50 = i

count = 0
maxSum = -1 * 10**34
for j in range(len(file) - 2):
    fst, snd, trd = file[j], file[j + 1], file[j + 2]

    arr = [fst, snd, trd]
    if len(arr) == len(set(arr)):
        flag = True
    else:
        flag = False

    count5 = 0
    for p in fst, snd, trd:
        if len(str(abs(p))) == 5:
            count5 += 1

    if flag and count5 == 3:
        if fst + snd + trd <= max50:
            count += 1
            if fst + snd + trd > maxSum:
                maxSum = fst + snd + trd

print(count, maxSum)
