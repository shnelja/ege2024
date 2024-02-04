def F(n):
    print('*')
    if n > 1:
        F(n - 2)
        F(n // 2)
        print('*')
    print('*')

