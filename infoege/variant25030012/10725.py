from itertools import product


def f(n):
    count = 0
    for i in range(2, n + 1, 2):
        if n % i == 0:
            count += 1
        if count >= 4:
            return True
    else:
        return False


def sumf(n):
    sum_ = 0
    for i in range(2, n + 1, 2):
        if n % i == 0:
            sum_ += i
    return sum_


digits = '0123456789'

c = 0
answer = []
try:
    for rep in range(3):
        for x in product(digits, repeat=rep):
            for q in digits:
                k = ''.join(x)
                if f(int(f'6{k}975{q}')):
                    answer.append(int(f'6{k}975{q}'))
                    c += 1
                    if c > 6:
                        raise StopIteration
except StopIteration:
    pass


answer = sorted(answer)
for x in answer:
    print(x, sumf(x))
