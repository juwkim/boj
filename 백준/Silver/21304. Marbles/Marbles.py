def comb2(n):
    return n * (n - 1) // 2

def solve():
    p, q, N, M = map(int, input().split())
    for total in range(N, M + 1):
        comb = comb2(total)
        for r in range(1, total // 2 + 1):
            g = total - r
            if r * g * q == p * comb:
                print(r, g)
                return
    print("NO SOLUTION")
solve()