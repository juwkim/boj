g = lambda: [*map(int, input().split())]


N, K = g()
cows = [int(input()) for _ in range(N)]

ans = -1
for i in range(N):
    num = cows[i]
    if num in cows[i+1:i+1+K]:
        ans = max(ans, num)
print(ans)