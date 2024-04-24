from itertools import product


def f(arr):
    result = []
    for x in arr:
        if x not in result:
            result.append(x)
    return result


hex_ = ''.join([hex(x)[2:] for x in range(16)])


count = 0
for x in product(hex_, repeat=3):
    res = ''.join(x)
    numb = []
    if res[0] != '0':
        for i in res:
            numb.append(hex_.index(i))
    if numb == sorted(numb)[::-1] and numb != []:
        if numb == f(numb):
            count += 1
            print(res, numb)

for x in product(hex_, repeat=5):
    res = ''.join(x)
    numb = []
    if res[0] != '0':
        for i in res:
            numb.append(hex_.index(i))
    if numb == sorted(numb)[::-1] and numb != []:
        if numb == f(numb):
            count += 1

print(count)
