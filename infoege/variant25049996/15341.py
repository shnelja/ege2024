file = [int(x) for x in open('files/26_15341.txt')]
file = sorted(file)[::-1]

answer1 = []
answer2 = []
for fst in range(len(file)):
    new = file[fst:len(file)]
    k = 0
    arr = [new[0]]
    for x in range(1, len(new)):
        if (new[k] - new[x]) >= 8:
            arr.append(new[x])
            k = x
    answer1.append(len(arr))
    answer2.append(arr[len(arr) - 1])

print(max(answer1), max(answer2))
