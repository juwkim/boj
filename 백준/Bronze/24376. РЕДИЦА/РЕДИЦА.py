x, n = map(int, input().split())
t = 1
n -= 1
while True:
    t *= x
    a = str(t)
    if len(a) >= n:
        print(a[n-1])
        break
    n -= len(a)