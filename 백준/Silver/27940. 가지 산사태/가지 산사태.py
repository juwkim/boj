N, M, K = map(int, input().split())

num = 0
ans = -1
for i in range(1, M + 1):
    t, r = map(int, input().split())
    num += r
    if num > K:
        ans = i
        break
if ans == -1:
    print(-1)
else:
    print(ans, 1)