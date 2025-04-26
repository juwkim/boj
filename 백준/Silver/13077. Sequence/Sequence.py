import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p, q = map(int, input().split('/'))
    n, w = 0, 1
    while p:
        if p < q:
            q -= p
        else:
            p -= q
            n += w
        w <<= 1
    print(n)