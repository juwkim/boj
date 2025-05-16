import sys
input = sys.stdin.readline

N = int(input())
dp = [bytearray(10) for _ in range(N + 1)]
for i in range(10):
    dp[0][i] = 1
for i in range(N):
    m, *a = map(int, input().split())
    alive = False
    for x in a:
        if any(p != x and q for p, q in enumerate(dp[i])):
            dp[i + 1][x] = 1
            alive = True
    if not alive:
        print(-1)
        break
else:
    ans = []
    prv = -1
    for i in range(N, 0, -1):
        j = 1
        while j == prv or dp[i][j] == 0:
            j += 1
        ans.append(j)
        prv = j
    print(*ans[::-1], sep='\n')