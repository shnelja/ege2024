file = [int(x) for x in open('C:/Users/Admin/source/repos/ege2024/infoege/task17/12926.txt')]

m2 = -100
for i in file:
    if len(str(abs(i))) == 2 and i > m2:
        m2 = i

A = -100000
for i in range(len(file) - 3):
    fst = file[i]
    snd = file[i + 1]
    trd = file[i + 2]
    fth = file[i + 3]
    last = abs(fst) % 10
    if abs(snd) % 10 == last and abs(trd) % 10 == last and abs(fth) % 10 == last and fst + snd + trd + fth > A:
        A = fst + snd + trd + fth

count = 0
for i in range(len(file) - 4):
    fst = file[i]
    snd = file[i + 1]
    trd = file[i + 2]
    fth = file[i + 3]
    ffth = file[i + 4]
    if fst < A + snd < A + trd < A + fth < A + ffth < A == 1 and (fst + snd + trd + fth + ffth) % m2 == 0:
        count += 1

print(count)
