g = lambda: [*map(int, input().split())]

while N:= int(input()):
    ps = [[0] * 1001 for _ in range(N)]
    for i in range(N):
        input()
        for num in g():
            ps[i][num] += 1
        for j in range(1, 1001):
            ps[i][j] += ps[i][j-1]
    ans = 1e9
    for j in range(0, 1001):
        ans = min(ans, sum(abs(ps[i][1000] - 2 * ps[i][j]) for i in range(N)))
    print(ans)