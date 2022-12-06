import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
for _ in range(int(input())):
    N = int(input())
    w1, w2, h1, h2 = g()
    ans = 'TAK'
    for _ in range(N - 1):
        a, b, c, d = g()
        if a <= w1 <= w2 <= b and c <= h1 <= h2 <= d:
            ans = 'TAK'
            w1, w2, h1, h2 = a, b, c, d
        elif w1 <= a <= b <= w2 and h1 <= c <= d <= h2:
            pass
        else:
            ans = 'NIE'
            w1, w2, h1, h2 = min(w1, a), max(w2, b), min(h1, c), max(h2, d)
    print(ans)