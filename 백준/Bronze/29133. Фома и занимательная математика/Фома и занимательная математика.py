a, b, c, d = map(int, input().split())
ans = [i for i in range(1, 4) if a ** i + b ** i + c ** i == d]
if len(ans) == 1:
    print(ans[0])
else:
    print(-1)