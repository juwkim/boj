import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

while n:=int(input()):
    ans, win = 0, 0
    p, q = 0, 0
    for a, b in zip(g(), g()):
        p += a
        q += b
        if p == q:
            continue
        if win:
            if win != (p > q) - (p < q):
                ans += 1
                win = (p > q) - (p < q)
        elif p > q:
            win = 1
        elif p < q:
            win = -1
    print(ans)