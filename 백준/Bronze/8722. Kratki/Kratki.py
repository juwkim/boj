import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

def solve(x):
    a, b = x
    if a > 2:
        a = 2 + (a - 2) // d
    if b > 2:
        b = 2 + (b - 2) // d
    p, q = x
    return (a * b, p * q)

n, d = g()
nums = [g() for _ in range(n)]

s, t = max(nums, key=solve)
print(s * t)