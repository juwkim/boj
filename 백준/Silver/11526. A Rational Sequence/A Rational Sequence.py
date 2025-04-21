import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K, l = input().split()
    p, q = map(int, l.split('/'))
    n, w = 0, 1
    while p:
        if p < q:
            q -= p
        else:
            n += w
            p -= q
        w <<= 1
    print(K, n)