file = [int(x) for x in open('2155.txt')]

max3 = max([int(x) for x in file if x % 3 == 0])

count = 0
maxSum = -1 * 10**34
for i in range(len(file) - 1):
    fst, snd = file[i], file[i + 1]

    count3 = 0
    for j in fst, snd:
        if j % 3 == 0 and j != max3:
            count3 += 1

    if count3 >= 1:
        count += 1
        maxSum = max(maxSum, fst + snd)

print(count, maxSum)
