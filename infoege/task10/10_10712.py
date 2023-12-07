s = open('10_10712_3.txt').read()
a = s.split()
cnt = 0
#print(a)
for i in range(len(a)):
    if ('Добр' in a[i] and 'Добр' != a[i] and '.' not in a[i] and ',' not in a[i] and '!' not in a[i] and '?' not in a[i] and ':' not in a[i] and '"' not in a[i] and ';' not in a[i]) or ('добр' in a[i] and 'добр' != a[i] and '.' not in a[i] and ',' not in a[i] and '!' not in a[i] and '?' not in a[i] and ':' not in a[i] and '"' not in a[i] and ';' not in a[i]):
        cnt += 1
        #print(i)
        #print(a[i])
print(cnt)