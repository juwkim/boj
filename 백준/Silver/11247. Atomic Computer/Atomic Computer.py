import sys
input = sys.stdin.readline

mem = {(0, 0): 1}
def solve(x, y):
    if (x, y) in mem:
        return mem[(x, y)]
    if x >= (1 << y) or x <= -(1 << y):
        return 0
    if x & 1:
        return solve(x + 1 >> 1, y - 1) + solve(x - 1 >> 1, y - 1)
    return solve(x >> 1, y - 1)

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(solve(x, y))