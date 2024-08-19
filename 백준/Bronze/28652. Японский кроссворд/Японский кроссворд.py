import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = [input() for _ in range(n)]
def solve(l):
    for s in l:
        buf = []
        cur = 0
        for c in s:
            if c == '#':
                cur += 1
            elif cur:
                buf.append(cur)
                cur = 0
        if cur:
            buf.append(cur)
        print(len(buf), *buf)
    print()

solve(a)
solve(zip(*a))