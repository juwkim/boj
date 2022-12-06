for i in range(1, 1+int(input())):
    D, N = map(int, input().split())
    t = []
    for _ in range(N):
        K, S = map(int, input().split())
        t.append((D - K) / S)
    print(f'Case #{i}: {D/max(t)}')