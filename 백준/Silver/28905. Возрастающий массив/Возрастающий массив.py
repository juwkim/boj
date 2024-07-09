n, *a = map(int, open(0).read().split())
a = [-abs(x) for x in a]
i = 0
while i < n - 1:
    if a[i] > a[i + 1]:
        for j in range(i + 1, n):
            a[j] = -a[j]
        break
    i += 1
if a == sorted(a):
    print("Yes")
    print(*a)
else:
    print("No")