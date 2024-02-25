def simple(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))


file = [int(x) for x in open('9993.txt')]
mult = []
max17 = max(x for x in file if abs(x) % 100 == 17)

for j in range(len(file) - 1):
    fst, snd = file[j], file[j + 1]
    if (simple(fst) + simple(snd)) == 1 and (fst + snd) % max17 == 0:
        mult.append(fst * snd)

print(len(mult), max(mult))
