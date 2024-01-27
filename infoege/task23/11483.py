from functools import lru_cache

@lru_cache(None)
def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    else:
        return f(x + 1, end) + f(x + 3, end) + f(x * 3, end)

print(f(3, 9) * f(9, 27) * f(27, 31))