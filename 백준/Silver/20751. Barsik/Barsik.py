g = lambda: [*map(int, input().split())]


for _ in range(int(input())):
    N, M, R, C, S = g()
    
    if (R + S < N and C - S > 1) or (R - S > 1 and C + S < M):
        ans = 'Barsik'
    else:
        ans = 'Tuzik'
    print(ans)