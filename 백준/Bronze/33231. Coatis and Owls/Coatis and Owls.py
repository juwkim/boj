n, m, *a = map(int, open(0).read().split())
i, j = n - 1, n
while i >= 0 and j < n + m:
    if a[i] < a[j]:
        a[j] -= (a[i]**2 + a[j] - 1) // a[j]
        i -= 1
    elif a[i] > a[j]:
        a[i] -= (a[j]**2 + a[i] - 1) // a[i]
        j += 1
    else:
        i -= 1
        j += 1
if i < 0 and j == n + m:
    print("stalemate")
elif i < 0:
    print("owls")
    print(sum(a[j:]))
else:
    print("coatis")
    print(sum(a[:i + 1]))