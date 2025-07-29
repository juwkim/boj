N, M = map(int, input().split())
if N + M == 2:
    print(-1)
elif N == 1:
    if M == 2:
        print(10**9 - 1)
        print(1, 10**9)
    else:
        print(M)
        print(*range(1, M), 10**9)
else:
    print(*range(1, N), 10**9)
    print(*range(N, N + M))