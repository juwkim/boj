from bisect import bisect_left

N, M = map(int, input().split())
px = [0] *(N + 1)
for i in range(N):
    px[i + 1] = px[i] + int(input())
ans = 1e9
for i in range(N):
    j = bisect_left(px, M + px[i])
    if j <= N:
        ans = min(ans, j - i)
print("NEPAVYKS" if ans == 1e9 else ans)