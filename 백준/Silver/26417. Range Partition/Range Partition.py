for tc in range(1, int(input()) + 1):
    N, X, Y = map(int, input().split())
    target, r = divmod(N * (N + 1) * X >> 1, X + Y)
    if r:
        print(f"Case #{tc}: IMPOSSIBLE")
        continue

    result = []
    for i in range(N, 0, -1):
        if target >= i:
            result.append(i)
            target -= i
        if target == 0:
            break
    if target:
        print(f"Case #{tc}: IMPOSSIBLE")
    else:
        print(f"Case #{tc}: POSSIBLE")
        print(len(result))
        print(*result)