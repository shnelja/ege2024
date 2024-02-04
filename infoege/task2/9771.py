print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                func = (not(y) or x) and not(z) and w
                if func == 1 or func == True:
                    print(x, y, z, w, func) # wxyz