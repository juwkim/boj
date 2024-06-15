import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

def solve():
    ax, ay = zip(*A)
    ap, aq = max(ax) - min(ax), max(ay) - min(ay)
    if bp * aq != bq * ap:
        return False
    for i in range(1, N):
        if (A[i][0] - A[0][0]) * bp != B[i][0] * ap or (A[i][1] - A[0][1]) * bq != B[i][1] * aq:
            return False
    return True

for _ in range(int(input())):
    N = int(input())
    A = sorted(g() for _ in range(N))
    B = sorted(g() for _ in range(N))
    B = [(B[i][0] - B[0][0], B[i][1] - B[0][1]) for i in range(N)]
    bx, by = zip(*B)
    bp, bq = max(bx) - min(bx), max(by) - min(by)
    ans = "mismatch!"
    for _ in range(4):
        if solve():
            ans = "okay"
            break
        A = sorted((y, -x) for x, y in A)
    print(ans)