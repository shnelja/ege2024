def treug(n, m, k):
    if max(n, m, k) < sum([x for x in [n, m, k] if x < max(n, m, k)]):
        return True
    else:
        return False


for a in range(1, 1000):
    if all(not(((treug(x, 11, 18)) == (not(max(x, 5) > 68))) and treug(x, a, 5)) for x in range(1, 1000)):
        print(a)
