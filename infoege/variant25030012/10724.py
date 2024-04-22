file = open('files/24_10724.txt').readline()

hex_ = [hex(x)[2:].upper() for x in range(16)]

fst = 0
answer = []
for snd in range(1, len(file)):
    new = file[fst:snd]
    if all(x in hex_ for x in new) and new[0] != '0':
        answer.append(len(new))
    else:
        fst += 1
print(max(answer))
