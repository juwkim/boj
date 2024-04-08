L, R = map(int, input().split())
ans = 0
m = 10**9 + 7
for i in range(L, R + 1):
    ans += pow(5, (i + 1) // 2, m)
    ans += pow(2, (i + 1) // 2, m)
    ans %= m
print(ans)