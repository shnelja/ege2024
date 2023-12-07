full_square = [c ** 2 for c in range(1, 1000)]

def f(n):
    return g(n - 1)

def g(n):
    if n < 10:
        return n
    if n >= 10:
        return g(n - 2) + 1
    
counter = 0
for i in range(1, 101):
    if f(i) in full_square:
        counter += 1

print(counter)