file = [int(x) for x in open('files/17_15333.txt')]

max19s = []
for x in file:
    if x % 19 == 0:
        max19s.append(x)
max19 = max(max19s)

sums = []
for i in range(len(file) - 1):
    fst, snd = file[i], file[i + 1]

    if fst > max19 or snd > max19:
        sums.append(fst + snd)

print(len(sums), max(sums))
