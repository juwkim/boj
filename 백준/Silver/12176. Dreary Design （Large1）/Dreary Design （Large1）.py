for t in range(1, 1 + int(input())):
    k, v = map(int, input().split())
    ans = 0
    for a in range(k + 1):
        for b in range(max(0, a - v), min(k, a + v) + 1):
            l = max(0, max(a, b) - v)
            r = min(k, min(a, b) + v)
            ans += r - l + 1
    print(f'Case #{t}: {ans}')