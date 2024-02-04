from itertools import product

n = 0
for c in product('БМНРЮ', repeat=6): 
    n += 1
    s = ''.join(c)
    if n % 2 != 0 and s[0] != 'М':
        if s.count('Р') >= 2 and 'Ю' not in s:
            index = n

print(index)