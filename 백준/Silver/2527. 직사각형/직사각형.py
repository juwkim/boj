import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def solve(x1, y1, p1, q1, x2, y2, p2, q2):
    if x2 > p1 or x1 > p2:
        return 'd'
    if y2 > q1 or y1 > q2:
        return 'd'
    if x2 == p1 or x1 == p2:
        if y2 == q1 or y1 == q2:
            return 'c'
        return 'b'
    if y2 == q1 or y1 == q2:
        return 'b'
    return 'a'

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = g()
    ans = solve(x1, y1, p1, q1, x2, y2, p2, q2)
    print(ans)