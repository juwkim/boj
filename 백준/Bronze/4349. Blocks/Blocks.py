for _ in range(int(input())):
    N = int(input())
    ans = 1e9
    for i in range(1, N+1):
        if N % i == 0:
            M = N // i
            for j in range(1, M + 1):
                if M % j == 0:
                    k = M // j
                    ans = min(ans, 2 * (i * j + j * k + k * i))
    print(ans)