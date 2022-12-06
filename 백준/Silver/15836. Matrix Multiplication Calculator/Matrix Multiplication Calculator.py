g = lambda: [*map(int, input().split())]

cnt = 1
while (s:= input()) != '0 0 0 0':
    M, N, P, Q = map(int, s.split())
    if N == P:
        A = [g() for _ in range(M)]
        B = [*zip(*[g() for _ in range(P)])]
        arr = [[0] * Q for _ in range(M)]
        for i in range(M):
            for j in range(Q):
                arr[i][j] = sum(s * t for s, t in zip(A[i], B[j]))
        
        print(f'Case #{cnt}:')
        for line in arr:
            print('|', *line, '|')
    else:
        for _ in range(M+P):
            input()
        print(f'Case #{cnt}:\nundefined')
    
    cnt += 1