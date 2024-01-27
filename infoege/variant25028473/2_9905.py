print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not(x) or y) and (not(y) or z) and (not(z) or w)
                if F == 1 or F == True:
                    print(x, y, z, w, F)