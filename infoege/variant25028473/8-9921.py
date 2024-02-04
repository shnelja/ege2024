from itertools import product

count = 0
n = 0
for c in product('ЕИКРСУЯ', repeat=6):
    n += 1
    s = ''.join(c)
    if n % 2 == 0 and s[0] != 'К' and s.count('Е') + s.count('И') + s.count('У') + s.count('Я') <= 2:
        count += 1

print(count)