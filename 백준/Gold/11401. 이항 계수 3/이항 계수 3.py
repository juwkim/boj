N, K = map(int, input().split())

mod = 10**9 + 7
ans = 1
for i in range(N - K + 1, N + 1):
    ans = (ans * i) % mod
for i in range(2, K + 1):
    ans = ans * pow(i, mod - 2, mod) % mod
print(ans)