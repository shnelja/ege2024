from functools import lru_cache

b = set()

@lru_cache(None)
def f(x, c):
    if c == 68:
        b.add(x)
        return
    f(x + 3, c + 1)
    f(x - 2, c + 1)

f(1, 0)
print(len(b))