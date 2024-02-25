file = [int(x) for x in open('2307.txt')]

three = []
seven = []
for i in file:
    if i % 7 == 0:
        seven.append(i)
    if i % 13 == 0:
        three.append(i)

if min(seven) > min(three):
    print(len(seven), max(seven))
else:
    print(len(three), max(three))
    