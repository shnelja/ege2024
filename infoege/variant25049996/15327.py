def f(n):
    bit = 27
    number = n
    arr = []
    while number > 0:
        arr.append(number % bit)
        number //= bit
    return arr[::-1]


count = 0
for i in f(3 * 2187**2020 + 3 * 729**2021 - 2 * 81**2022 + 27**2023 - 4 * 3**2024 - 2029):
    if i > 9:
        count += 1
print(count)
