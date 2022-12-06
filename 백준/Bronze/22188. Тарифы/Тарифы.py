g = lambda: [*map(int, input().split())]

def solve(x):
    c, t, p = cost[x]
    ans = 100 * c
    for time in times:
        k = (time + t - 1) // t - (time < t)
        ans += p * k
    return ans


n, m = g()
cost = [g() for _ in range(n)]
times = g()

print(1 + min(range(n), key=solve))