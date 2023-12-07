print('a b c t F')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for t in 0, 1:
                func = (not(a) or not(b)) and (not(c) or not(a)) and (t and not(a) or c and not(b))
                if (func == 0 or func == False) and (0 < a + b + c + t < 3):
                    print(a, b, c, t, func)
print()

print('a b c t F')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for t in 0, 1:
                func = (not(a) or not(b)) and (not(c) or not(a)) and (t and not(a) or c and not(b))
                if (func == 1 or func == True) and (a + b + c + t == 3 or a + b + c + t == 1):
                    print(a, b, c, t, func) # ctab