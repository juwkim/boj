n, K, *a = map(int, open(0).read().split())
a.sort(reverse=True)
ans = n
for i in range(n - 1):
    if a[i] - a[i + 1] > K:
        ans = i + 1
        break
print(ans)