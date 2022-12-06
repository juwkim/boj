if (N:=int(input()))%2:
    s = N//2
    print('\n'.join(['*' * N, ' ' * s + '*']))
    for i in range(s):
        print(' ' * (s - i - 1) + (' ' * (2*i + 1)).center(2*i+3, '*'))
else:
    print('I LOVE CBNU')