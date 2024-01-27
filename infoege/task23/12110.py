from math import sqrt
from functools import lru_cache

@lru_cache(None)
def f(s, e):
    if s <= e or s == 4 or s == 43:
        return s == e
    else:
        return f(s - 1, e) + f(s // 3, e) + f(int(sqrt(s)), e)
    
print(f(98, 14) * f(14, 2))