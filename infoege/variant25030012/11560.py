print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x or not(y)) and not(x == z) and w
                if f == 1 or f == True:
                    print(x, y, z, w, f)
                    