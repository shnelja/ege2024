s = open('10_4322.txt').read()
a = s.split()
ctr = 0
for i in range(len(a)):
    if ('В' in a[i] or 'в' in a[i]) and ('А' not in a[i]) and ('а' not in a[i]) and ('О' not in a[i]) and ('о' not in a[i]):
        ctr += 1
print(ctr)
