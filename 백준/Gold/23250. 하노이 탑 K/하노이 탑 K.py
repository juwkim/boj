def hanoi(n, a, b, c, K):
    n -= 1
    check = (1 << n)
    if n == 0 or K == check:
        print(a, c)
    elif K < check:
        hanoi(n, a, c, b, K)
    else:
        hanoi(n, b, a, c, K - check)

N, K = map(int, input().split())
hanoi(N, 1, 2, 3, K)