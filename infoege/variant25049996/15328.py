def f(n):
    bit = 27
    arr = n[::-1]
    ans = 0
    for i in range(len(n)):
        ans += arr[i] * bit ** i
    return ans


for x in range(27):
    if (f([1, 2, 3, x, 2, 4]) + f([1, 3, 5, x, 7, 8])) % 26 == 0:
        print(x, (f([1, 2, 3, x, 2, 4]) + f([1, 3, 5, x, 7, 8])) / 26)
