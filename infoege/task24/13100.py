file = open('13100.txt').readline()

result = []
countC, countD = 0, 0
for i in range(len(file)):
    line = ''
    for j in range(i, len(file)):
        if file[j] == 'C':
            countC += 1
        if file[j] == 'D':
            countD += 1
        if countD > 2 or countC > 2:
            countC, countD = 0, 0
            break

        line += file[j]
    result.append(line)

lens = [len(x) for x in result]
print(max(lens))
