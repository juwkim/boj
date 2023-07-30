g = lambda: [*map(int, input().split())]

while True:
    N, M = g()
    if N == 0:
        break
    A = [g() for _ in range(N)]
    B = [g() for _ in range(N)]
    
    ans = []
    for i in range(N):
        max_Bi = max(B[i])
        for j, num in enumerate(B[i]):
            if num != max_Bi:
                continue
            if all(A[i][j] >= A[k][j] for k in range(N)):
                ans.append((i + 1, j + 1))
    print(len(ans))
    for line in ans:
        print(*line)