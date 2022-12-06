for _ in[0]*int(input()):
    N = int(input())
    print('YES' if N**2 % 10**(len(str(N))) == N else 'NO')