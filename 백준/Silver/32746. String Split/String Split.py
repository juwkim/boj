import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s, t = input(), input()
    def solve(a, b):
        if len(a) < len(b):
            return 0
        if len(a) == len(b):
            return a == b
        return solve(a[::2], b) or solve(a[1::2], b)
    print("YES" if solve(s, t) else "NO")