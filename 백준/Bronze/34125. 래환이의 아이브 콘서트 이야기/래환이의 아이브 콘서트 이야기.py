N, M = map(int, input().split())
ans = 1e9, 1e9, 1e9
for i in range(1, N + 1):
    for j, c in enumerate(input().split(), 1):
        if c == '0':
            ans = min(ans, (i + abs((M + 1) // 2 - j), i, j))
if ans[0] == 1e9:
    print(-1)
else:
    print(*ans[1:])