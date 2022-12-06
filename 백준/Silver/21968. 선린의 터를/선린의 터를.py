for _ in range(int(input())):
    N = int(input())
    ans, cur = 0, 1
    while N:
        ans += cur * (N % 2)
        N //= 2
        cur *= 3
    print(ans)