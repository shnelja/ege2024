print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                func = not(y) and (not(x) or (not(z) == w)) or z
                if (func == 0 or func == False) and 0 < x + y + z + w < 3:
                    print(x, y, z, w, func) # yxwz