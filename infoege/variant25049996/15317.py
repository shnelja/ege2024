def algorithm(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '01'
    else:
        r = '1' + r + '1'
    return int(r, 2)


print(f'example: {algorithm(12)}, {algorithm(5)}')
for i in range(200):
    if algorithm(i) > 156:
        print(f'answer: {i}, {algorithm(i)}')
        break
