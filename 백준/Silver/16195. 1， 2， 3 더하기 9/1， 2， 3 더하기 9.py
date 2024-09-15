import sys
input = sys.stdin.readline

mem = {}
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
    mem[(a, b)] = (solve(a - 1, b - 1) + solve(a - 2, b - 1) + solve(a - 3, b - 1)) % 1_000_000_009
    return mem[(a, b)]
for _ in range(int(input())):
    print(solve(*map(int, input().split())))