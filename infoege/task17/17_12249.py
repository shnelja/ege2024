file = open('C:/Users/Admin/source/repos/ege2024/infoege/task17/17_12249.txt').read()
file = file.split()

max5 = 0
for i in file:
    element = int(i)
    if element > max5 and i[len(i) - 1] == '3' and 9999 < abs(element) < 100000:
        max5 = element

counter = 0
max_sum = 0
for j in range(len(file) - 2):
    three1 = int(file[j])
    three2 = int(file[j + 1])
    three3 = int(file[j + 2])
    sum = three1 + three2 + three3
    if (abs(three1) % 10 == 3 or abs(three2) % 10 == 3 or abs(three3) % 10 == 3) and sum <= max5:
        counter += 1
        if sum > max_sum:
            max_sum = sum

print(counter)
print(max_sum)
