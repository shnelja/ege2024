counter = 0

for n in range(3, 1000):

    s = '3' + n * '5'
    sum = 0

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)

    for c in s:
        sum += int(c)
    
    count = 0
    for i in range(1, sum + 1):
        if sum % i == 0:
            count += 1
    
    if count == 2:
        counter += 1
    
print(counter)