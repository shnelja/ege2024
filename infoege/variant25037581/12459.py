def tera(x):
    number = x
    bit = 4
    result = ''
    while number > 0:
        result += str(number % bit)
        number //= bit
    return result[::-1]


for n in range(1, 1000):
    r = tera(n)
    if len(r) % 2 == 0:
        r = r[0:len(r)//2] + '0' + r[len(r)//2:len(r)]
    if int(r) <= 180:
        print(n)
