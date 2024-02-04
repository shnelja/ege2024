print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                func = (not(not(w) or y) or (x == y)) or not(z)
                if func == 0 or func == False:
                    print(x, y, z, w, func) # xyzw