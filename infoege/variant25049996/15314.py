print('w x y z F')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = (x and not z) or (y == z) or not w
                if not f:
                    print(w, x, y, z, f)
