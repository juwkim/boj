import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

while N:=int(input()):
    A, B, C, D = g()
    x, y = g()
    dist_to_box = lambda a, b: max(0, a - C, A - a) + max(0, b - D, B - b)
    ans = 0
    for _ in range(N):
        nx, ny = g()
        if A <= x <= C and B <= y <= D:
            ans += dist_to_box(nx, ny)
        elif A <= nx <= C and B <= ny <= D:
            ans += dist_to_box(x, y) - 1
        else:
            dx, dy = (nx > x) - (nx < x), (ny > y) - (ny < y)
            cnt1 = dist_to_box(nx, ny) + dist_to_box(x, y) - 1
            cnt2 = 0
            while x != nx:
                x += dx
                cnt2 += not (A <= x <= C and B <= y <= D)
            while y != ny:
                y += dy
                cnt2 += not (A <= x <= C and B <= y <= D)
            ans += min(cnt1, cnt2)
        x, y = nx, ny
    print(ans)