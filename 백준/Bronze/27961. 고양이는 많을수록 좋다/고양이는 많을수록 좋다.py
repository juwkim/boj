N = int(input())

if N == 0:
    print(0)
else:
    ans = 1
    t = 1
    while t < N:
        t <<= 1
        ans += 1
    print(ans)