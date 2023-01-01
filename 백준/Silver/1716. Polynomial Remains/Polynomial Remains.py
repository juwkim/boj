def g(): return [*map(int, input().split())]

while (l:= g()) != [-1, -1]:
    n, k = l
    a = g()
    for i in range(n - k, -1, -1):
        a[i] -= a[i + k]
        a[i + k] = 0
    print(*a[:max(k,1)])