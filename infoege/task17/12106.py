file = [int(x) for x in open('12106.txt')]

threes = []
for i in file:
    if i > 0 and i % 117 == 0:
        threes.append(i)

count = 0
squares = []
for j in range(len(file) - 1):
    fst, snd = file[j], file[j + 1]

    countNegative = 0
    for p in fst, snd:
        if p < 0:
            countNegative += 1

    if countNegative == 1:
        if abs(fst + snd) % abs(min(threes)) == 0:
            count += 1
            squares.append(fst**2 + snd**2)

print(count, min(squares))
