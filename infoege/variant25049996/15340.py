from itertools import product

digits = '012345678'

answer = []
for q in digits:
    for x in product(digits, repeat=3):
        line = ''.join(x)
        if int(f'1{line}2322{q}2') % 2024 == 0:
            answer.append(int(f'1{line}2322{q}2'))

for x in sorted(answer):
    print(x, x//2024)
