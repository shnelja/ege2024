from itertools import product

digits = '0123456789'
for i in range(4):
    for x in product(digits, repeat=i):
        for q in digits:
            line = ''.join(x)
            mask = f'1{line}2322{q}2'
            if int(mask) % 2024 == 0:
                print(mask, int(mask) // 2024)
