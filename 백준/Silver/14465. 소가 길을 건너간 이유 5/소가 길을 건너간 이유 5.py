N, K, B = map(int, input().split())
arr = [1] * N
for _ in range(B):
    arr[int(input()) - 1] = 0
cur = sum(arr[:K])
ans = cur
for i in range(K, N):
    cur = cur + arr[i] - arr[i - K]
    ans = max(ans, cur)
print(K - ans)