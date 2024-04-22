file = open('14645.txt').readline()

c = 'BCDFGHJKLMNPQRSTVWXZ'
v = 'AEIOUY'

fst = 0
answer = []
for snd in range(2, len(file) + 1):
    new = file[fst:snd]
    if all((not ((new[x] in c and new[x + 1] in c) or (new[x] in v and new[x + 1] in v))) for x in range(len(new) - 1)):
        answer.append(len(new))
    else:
        fst += 1

print(answer)
