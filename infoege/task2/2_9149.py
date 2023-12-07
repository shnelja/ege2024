print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                func = ((not(x) or y) or (z == x)) and (not(w) or z)
                if (func == 1 or func == True) and x + y + z + w == 2:
                    print(x, y, z, w, func)
print()

print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                func = ((not(x) or y) or (z == x)) and (not(w) or z)
                if (func == 0 or func == False) and (x + y + z + w == 3 or x + y + z + w == 1):
                    print(x, y, z, w, func) # zwxy