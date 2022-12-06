n = int(input())
if n < 2:
    print(1 - n)
else:
    r, q = divmod(n, 2)
    print('4' * q + '8' * r)