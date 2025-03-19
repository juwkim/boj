import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
d = lambda num: y1 + (num - x1) * (y2 - y1) / (x2 - x1) - (v1 + (num - u1) * (v2 - v1) / (u2 - u1))

for _ in range(int(input())):
    n = int(input()); xy = g()
    m = int(input()); uv = g()
    ans, idx = float('inf'), 0
    for i in range(0, 2 * (m - 1), 2):
        u1, v1 = uv[i], uv[i + 1]
        u2, v2 = uv[i + 2], uv[i + 3]
        while True:
            x1, y1 = xy[idx], xy[idx + 1]
            x2, y2 = xy[idx + 2], xy[idx + 3]
            p, q = max(u1, x1), min(u2, x2)            
            ans = min(ans, d(p), d(q))
            if x2 <= u2:
                idx += 2
            if x2 >= u2:
                break
    print(f"{ans:.2f}")