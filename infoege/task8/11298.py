from itertools import product

n = cnt = 0 # вместе с переменной номера объявляем переменную счетчика
for c in product('АЖЗОПЮ', repeat=6):
    n += 1 # добавляем 1 к номеру в начале тела цикла, так как нумерация по условию начинается с 1
    s = ''.join(c)
    if n % 2 == 0 and s[0] == 'А' and s.count('З') >= 2:
        cnt += 1 # если условие верно к счетчику добавляем 1

print(cnt)