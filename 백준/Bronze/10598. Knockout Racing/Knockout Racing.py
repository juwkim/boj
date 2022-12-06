n, m = map(int, input().split())
start = [[*map(int, input().split())] for _ in range(n)]
for _ in range(m):
    x, y, t = map(int, input().split())
    print(sum(1 for a, b in start if x <= min(a + t%(2*b-2*a), 2*b - a - t%(2*b-2*a)) <= y))