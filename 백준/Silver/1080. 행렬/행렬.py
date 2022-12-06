g = lambda: [*map(int, input().split())]
N, M = map(int, input().split())

A = [[int(i) for i in input().rstrip()] for _ in range(N)]
B = [[int(i) for i in input().rstrip()] for _ in range(N)]
ans = 0
if A != B:
    if N < 3 or M < 3:
        ans = -1
    else:
        for i in range(N-2):
            for j in range(M-2):
                if A[i][j] == B[i][j]:
                    continue
                for s in range(i, i+3):
                    for t in range(j, j+3):
                        A[s][t] ^= 1
                ans += 1
    if A != B:
        ans = -1
print(ans)