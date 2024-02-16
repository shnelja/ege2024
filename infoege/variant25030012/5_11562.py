def six(n):
    res = ''
    while n != 0:
        res += str(n % 6)
        n //= 6
    return res[::-1]

def dec(n):
    res = 0
    pencil = len(n) - 1
    for c in n:
        res += int(c) * 6 ** pencil
        pencil -= 1
    return res

for number in range(1, 1000):
    number_six = six(number)
    if number % 3 == 0:
        number_six += number_six[0:2]
    else:
        number_six += six((int(number) % 3) * 10)
    
    if dec(number_six) > 680:
        print(dec(number_six))
        break
