import re

s = open('c:/Users/Admin/source/repos/ege2024/infoege/task10/10_7363.txt').read()
a = re.sub(r'[^\w\s]', '', s)
a = a.split()
cnt = 0
for i in range(len(a)):
        if ('рыба' in a[i] and 'рыба' != a[i]) or ('Рыба' in a[i] and 'Рыба' != a[i]):
            cnt += 1
print(cnt)
