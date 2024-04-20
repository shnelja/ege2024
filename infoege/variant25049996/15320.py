from itertools import product

arr = sorted([x for x in 'парус'])
alpha = ''.join(arr)[::-1]

n = 0
for i in product(alpha, repeat=5):
    line = ''.join(i)
    n += 1
    if line.count('а') == 0 and line.count('у') <= 1:
        print(f'{n}. {line}')
        break
