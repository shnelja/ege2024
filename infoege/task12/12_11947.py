for n in range(3, 10001):
    s = '5' + '2' * n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11')
        if '2222' in s:
            s = s.replace('2222', '5')
        if '1122' in s:
            s = s.replace('1122', '25')
    sm = sum(int(c) for c in s)
    if sm == 64:
        index = n

print(index)