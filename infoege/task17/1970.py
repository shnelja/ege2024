def divisibility(n):
    if abs(n) % 3 == 0:
        return True
    return False


file = [int(x) for x in open('1970.txt')]

count = 0
sums = []
for i in range(len(file) - 1):
    fst, snd = file[i], file[i + 1]
    if (divisibility(fst) + divisibility(snd)) >= 1:
        count += 1
        sums.append(fst + snd)

print(count, max(sums))
