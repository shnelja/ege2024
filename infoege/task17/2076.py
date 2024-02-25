file = [int(x) for x in open('2076.txt')]

count = 0
hypSum = 0
for j in range(len(file) - 2):
    three = sorted([file[j], file[j + 1], file[j + 2]])

    if three[2]**2 == three[1]**2 + three[0]**2:
        count += 1
        hypSum += three[2]

print(count, hypSum)
