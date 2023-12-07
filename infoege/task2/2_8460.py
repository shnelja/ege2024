print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                func = ((x == z) or not(x == w)) and ((not(y) or x) or not(z))
                if func == 0 or func == False:
                    print(x, y, z, w, func) # xzwy