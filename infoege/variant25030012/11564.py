def f(n, bit):
    new = n[::-1]
    sum_ = 0
    for i in range(len(new)):
        sum_ += new[i] * bit ** i
    return sum_


for x in range(150):
    if (f([5, 1, x, 2, 9], 150) + f([x, 0, 2, 3], 150)) % 149 == 0:
        print((f([5, 1, x, 2, 9], 150) + f([x, 0, 2, 3], 150)) // 149)
