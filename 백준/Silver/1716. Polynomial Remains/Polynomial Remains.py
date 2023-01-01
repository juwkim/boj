def g(): return [*map(int, input().split())]

while (l:= g()) != [-1, -1]:
    n, k = l
    a = g()
    for i in range(n - k, -1, -1):
        a[i] -= a[i + k]
        a[i + k] = 0
        
    if a[0] == 0:
        print(0)
    else:
        for i in range(n + 1):
            if a[i] == 0:
                break
            print(a[i], end=' ')
        print()