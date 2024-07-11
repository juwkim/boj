import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = input()
    def solve(l, r):
        if l == r:
            return True
        n = (r - l) // 2
        if any(s[l + i] == s[r - i] for i in range(n)):
            return False
        return solve(l, l + n - 1) and solve(l + n + 1, r)
    print("YES" if solve(0, len(s) - 1) else "NO")