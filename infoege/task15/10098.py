for a in range(1, 500):
    cnt = 0
    for x in range(1, 501):
        for y in range(1, 501):
            func = (x + 2 * y < a) or (y > x) or (x > 60)
            if func:
                cnt += 1
        if cnt == 250000:
            print(a)  # ответ 181
