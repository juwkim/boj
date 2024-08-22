import sys

mem = {}
def solve(n, s):
    if (n, s) in mem:
        return mem[(n, s)]
    if s < 0:
        return 0
    if n == 1:
        return 0 <= s < 10
    mem[(n, s)] = sum(solve(n - 1, s - i) for i in range(10))
    return mem[(n, s)]

for l in sys.stdin:
    n, s = map(int, l.split())
    print(solve(n, s))