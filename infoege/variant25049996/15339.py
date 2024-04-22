file = open('files/24_15339.txt').readline()

alpha = 'ABC'
digits = '6789'

arr = []
fst = 0
for snd in range(2, len(file) + 1):
    new = file[fst:snd]
    for x in range(1, len(new)):
        if (new[x - 1] in digits and new[x] in digits) or (new[x - 1] in alpha and new[x] in alpha):
            fst += 1
            break
    else:
        arr.append(len(new))

print(max(arr))
