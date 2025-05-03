import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
A = [int(input()) for _ in range(a)]
B = [int(input()) for _ in range(b)]
C = [int(input()) for _ in range(c)]
D = [int(input()) for _ in range(d)]

def solve():
    ab = {}
    for x in A:
        for y in B:
            ab[-x - y] = x, y
    for x in C:
        for y in D:
            target = x + y
            if target in ab:
                a1, b1 = ab[target]
                print(a1, b1, x, y)
                return
solve()