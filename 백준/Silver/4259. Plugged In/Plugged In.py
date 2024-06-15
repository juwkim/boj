import sys
input = sys.stdin.readline
dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + 1

tc = 1
while n:=int(input()):
    a, b = [], []
    m = int(input())
    for _ in range(m):
        p, q = map(lambda x: int(x) - 1, input().split())
        a.append(divmod(p, n))
        b.append(divmod(q, n))
    ans = float("inf")
    for _ in range(4):
        ans = min(ans, sum(dist(p1, p2) for p1, p2 in zip(a, b)))
        ans = min(ans, sum(dist(p1, (p2[0], n - 1 - p2[1])) for p1, p2 in zip(a, b)))
        b = [(p[1], n - 1 - p[0]) for p in b]
    print(f"Scenario {tc}: smallest average = {ans / m:.4f}\n")
    tc += 1