file = [int(x) for x in open('2308.txt')]

odds = []
evens = []
for i in file:
    if i % 2 != 0:
        odds.append(i)
    else:
        evens.append(i)

if max(evens) > max(odds):
    print(len(evens), min(evens))
else:
    print(len(odds), min(odds))
