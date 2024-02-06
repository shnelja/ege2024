def move_zeros(lst):
    result = []
    count = 0
    for i in lst:
        if i != 0:
            result += [i]
        else:
            count += 1
    for j in range(count):
        result += [0]
    return result

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))