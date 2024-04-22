file = open('14647.txt').readline()

fst = 0
answer = []
for snd in range(2, len(file) + 1):
    new = file[fst:snd]
    if new.count('X') > 1 or new.count('Y') > 1:
        fst += 1
    elif new.count('X') == 1 and new.count('Y') == 1:
        answer.append(len(new))

print(max(answer))
