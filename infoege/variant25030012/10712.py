import re

s = open('c:/Users/Admin/source/repos/ege2024/infoege/variant25030012/files/10_10712_3.txt').read()
a = re.sub(r'[^\w\s]', '', s)
a = a.split()
cnt = 0
for i in range(len(a)):
    if ('добр' in a[i] and 'добр' != a[i]) or ('Добр' in a[i] and 'Добр' != a[i]):
        cnt += 1
print(cnt)