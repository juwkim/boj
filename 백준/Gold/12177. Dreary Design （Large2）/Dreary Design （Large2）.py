for t in range(1, 1 + int(input())):
    k, v = map(int, input().split())
    ans = 0
    if v >= k:
        ans = (k + 1) ** 3
    else:
        ans = (3 * v * (v + 1) + 1) * (k - v + 1 ) + v ** 3
    print(f'Case #{t}: {ans}')