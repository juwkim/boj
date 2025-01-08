n, *a = map(int, input().split())
b = sorted(a)
sum1, sum2 = 0, 0
ans = []
for i in range(n):
    if a[i] == b[i] and sum1 == sum2:
        ans.append(a[i])
    sum1 += a[i]
    sum2 += b[i]
print(len(ans), *ans[:100])