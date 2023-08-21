N, M = map(int, input().split())
r = range(N - M, N + 1)
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        num = int(str(j) * i)
        if num in r:
            ans += 1
print(ans)