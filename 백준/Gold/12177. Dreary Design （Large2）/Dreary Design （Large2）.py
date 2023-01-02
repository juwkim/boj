for t in range(1, 1 + int(input())):
    k, v = map(int, input().split())
    ans = (3 * v * (v + 1) + 1) * max(0, k - v) + (min(k, v) + 1) ** 3
    print(f'Case #{t}: {ans}')