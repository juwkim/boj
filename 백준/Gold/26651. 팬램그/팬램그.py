X = int(input())
if X:
    i = 1
    while X >= (i + 1)**2:
        i += 1
    for j in range(i, 0, -1):
        if X >= j**2:
            q, X = divmod(X, j**2)
            s = ('A' * j + 'BCDEFGHIJKLMNOPQRSTUVWXY' + 'Z' * j) * q
            print(s, end='')
else:
    print('A')