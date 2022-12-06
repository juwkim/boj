g = lambda x: (x % 100 - 1) % 100 // 4 
while (s:=input()) != '0 0 0':
    V, N, M = s.split()
    N, M = map(int, [N, M])
    if N % 10000 == M % 10000:
        res = 3000
    elif N % 1000 == M % 1000:
        res = 500
    elif N % 100 == M % 100:
        res = 50
    elif g(N) == g(M):
        res = 16
    else:
        res = 0
    print(f'{float(V) * res:#.2f}')