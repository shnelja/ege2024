print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                func = (x or not(y)) and not(x == z) and w
                if func == 1 or func == True:
                    print(x, y, z, w, func) # zyxw