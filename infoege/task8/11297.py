from itertools import product

n = 0
for c in product('ИРЩЮ', repeat=5):
    n += 1
    s = ''.join(c)
    if s[0] == 'Щ' and s[len(s) - 1] == 'И':
        index = n

print(index)