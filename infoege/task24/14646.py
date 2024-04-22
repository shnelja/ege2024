file = open('14646.txt').readline()

x = 0
arr = []
for i in range(len(file)):
    new = file[x:x + 4]
    if 3*new[0] in new:
        arr.append(new[3])
        x += 1
    else:
        x += 1
print(arr)

count = 0
for i in arr:
    if arr.count(i) > count:
        count = arr.count(i)
        print(i+str(count))
