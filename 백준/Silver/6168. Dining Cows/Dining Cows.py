N = int(input())
a = [0]
for _ in range(N):
    a.append(a[-1] + int(input()))
ans = 1e9
for i in range(N+1):
    ans = min(ans, 2 * a[i] - a[N] - 3 * i)
print(ans + 2 * N)