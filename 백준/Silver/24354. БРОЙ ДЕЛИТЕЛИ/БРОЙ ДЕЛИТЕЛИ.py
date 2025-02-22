n = int(input())
a = [1] * (n + 1)
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        a[j] += 1
idx = max(range(1, n + 1), key=lambda x: (a[x], -x))
print(idx)
print(a[idx])