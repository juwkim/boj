N = int(input())
a, n = '*', '\n'
if N == 1:
    print(a)
else:  
    print(a * N)
    for i in range(N//2-1):
        p = ' ' * i
        print(a + p + a + ' ' * (N - 4 - 2 * i) + a + p + a)
    if N % 2:
        p = (N - 3) // 2 * ' '
        print(a + p + a + p + a)
    for i in range(N//2-2, -1, -1):
        p = ' ' * i
        print(a + p + a + ' ' * (N - 4 - 2 * i) + a + p + a)
    print(a * N)