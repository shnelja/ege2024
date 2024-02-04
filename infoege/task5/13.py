def digitalSum(n):
    if n < 10 :
        return n
    return n % 10 + digitalSum( n // 10 )


for n in range(1, 501):
    r = bin(n)[2:]
    r0 = n
    for i in range(2):
        if digitalSum(int(r)) % 2 == 0:
            r0 *= 2
        else:
            r0 *= 2
            r0 += 1
    if r0 > 77:
        print(n)
        break
