import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, n = map(int, input().split())
    b, cur = 0, 0
    for i in range(60, -1, -1):
        p = 1 << i
        cur ^= p & a
        l, r = cur, cur + p - 1
        if l > r - r % n:
            cur ^= p
            b ^= p
    print(b)