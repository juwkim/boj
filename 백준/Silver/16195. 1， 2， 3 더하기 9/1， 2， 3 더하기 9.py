import sys
input = sys.stdin.readline

mod = 1_000_000_009
mem = {}
for _ in range(int(input())):
    n, m = map(int, input().split())
    assert n >= 0 and m >= 0 and m <= n
    def solve(a, b):
        if (a, b) in mem:
            return mem[(a, b)]
        if a < 0:
            return 0
        if a == 0:
            return 1
        if a > 3 * b:
            return 0
        if b == 1:
            return +(a <= 3)
        mem[(a, b)] = (solve(a - 1, b - 1) + solve(a - 2, b - 1) + solve(a - 3, b - 1)) % mod
        return mem[(a, b)]
    print(solve(n, m))