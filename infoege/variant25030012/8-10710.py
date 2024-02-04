from itertools import product

answer = index = 0
for c in product('екмопртью', repeat=5):
    index += 1
    s = ''.join(c)
    if index % 2 != 0:
        if s[0] != 'ь' and s.count('к') == 2:
            answer = index

print(answer)