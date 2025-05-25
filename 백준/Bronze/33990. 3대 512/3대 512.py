ans = 1e9
for _ in range(int(input())):
    P = sum(map(int, input().split()))
    if P >= 512:
        ans = min(ans, P)
if ans == 1e9:
    print(-1)
else:
    print(ans)