def parity(n):
    if abs(n) % 2 == 0:
        return True
    return False


file = [int(x) for x in open('1997.txt')]

count = 0
sums = []
for i in range(len(file) - 1):
    fst, snd = file[i], file[i + 1]
    if parity(fst) + parity(snd) == 1:
        for p in fst, snd:
            if parity(p):
                if abs(p) % 4 == 0:
                    fstFlag = True
                else:
                    fstFlag = False
            else:
                if abs(p) % 11 == 0:
                    sndFlag = True
                else:
                    sndFlag = False

        if fstFlag and sndFlag:
            count += 1
            sums.append(fst + snd)

print(count, max(sums))
