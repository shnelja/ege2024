from itertools import permutations

valid_symbols = 'АЕМНОР123456789'

digits = '123456789'
characters = 'АЕМНОР'

base = []
for i in permutations(valid_symbols, 7):
    a = ''.join(i)
    if a[0:4:1] in digits and a[4:7:1] in characters:
        base += [a]