N = int(input())
a = [*map(int, input().split())]
ans = 0
for i in range(N):
    if not a[i]:
        continue
    ans += 1
    a[i] ^= 1
    if i + 1 < N: a[i + 1] ^= 1
    if i + 2 < N: a[i + 2] ^= 1
print(ans)