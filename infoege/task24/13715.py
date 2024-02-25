file = open('13715.txt').readline()

result = []
for i in range(len(file)):
    count = 0
    count1 = 0
    for j in range(i, len(file)):
        count1 += 1
        if j != len(file) - 1:
            if file[i] + file[j + 1] == 'AB':
                count += 1
                if count >= 50:
                    result.append(count1)
                    break

print(max(result))
