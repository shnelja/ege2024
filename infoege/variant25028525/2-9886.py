print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((not(x) or y) == w) or (not(y) and z)
                if F == 0 or F == False:
                    print(x, y, z, w, F)