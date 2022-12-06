for _ in range(int(input())):
    K, N = map(int, input().split())
    print(K, N * (N + 3) // 2)