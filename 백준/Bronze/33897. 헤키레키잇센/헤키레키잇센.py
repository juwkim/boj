N, *a = map(int, open(0).read().split())
cnt, Max = 1, 1
cur = 1
for i in range(1, N):
    if a[i] < a[i - 1]:
        cnt += 1
        cur = 1
    else:
        cur += 1
        Max = max(Max, cur)
print(cnt, Max)