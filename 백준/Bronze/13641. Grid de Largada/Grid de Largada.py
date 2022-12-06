g = lambda: [*map(int, input().split())]

while True:
    try:
        N = int(input())
        a = g()
        b = g()
        ans = 0
        for i in range(N-1, 0, -1):
            idx = b.index(a[i])
            ans += i - idx
            b.insert(i, b.pop(idx))
        print(ans)
    except:
        break