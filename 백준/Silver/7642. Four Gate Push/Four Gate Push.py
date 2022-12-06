while sum(nums := [*map(int, input().split())]):
    M, G, Z, S, E = nums
    ans = 0
    for r in range(1 + min(M // 50, G // 100)):
        for q in range(1 + min((G - 100 * r) // 50, (M - 50 * r) // 125)):
            p = (M - 50 * r - 125 * q) // 100
            ans = max(ans, p*Z + q*S +r*E)
    print(ans)