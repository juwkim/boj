N, M, K = map(int, input().split())
if K < N + M - 1:
    print('NO')
else:
    print('YES')
    for i in range(1, 1 + N):
        print(*range(i, i + M))