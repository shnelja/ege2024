file = [int(x) for x in open('1996.txt')]

count = 0
middle = []
for i in range(len(file) - 1):
    fst, snd = file[i], file[i + 1]

    if abs(fst * snd) % 2 != 0 and abs((fst + snd) / 2) % 7 == 0:
        count += 1
        middle.append((fst + snd) / 2)

print(count, min(middle))
