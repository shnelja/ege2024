print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                func = (x or y and not(z)) and not(w)
                if x + y + z + w == 1 and (func == 1 or func == True):
                    print(x, y, z, w, func)
print()

print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                func = (x or y and not(z)) and not(w)
                if x + y + z + w == 2 and (func == 0 or func == False):
                    print(x, y, w, z, func)

# 4