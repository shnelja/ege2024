print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                func = not(not(y) or z) or (x or not(w)) or x
                if func == 0 or func == False:
                    print(x, y, z, w, func) # ywzx