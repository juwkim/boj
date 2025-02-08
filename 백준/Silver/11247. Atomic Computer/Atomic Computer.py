import sys
input = sys.stdin.readline

mem = {}
def solve(x, y):
    if (x, y) in mem:
        return mem[(x, y)]
    if x >= (1 << y) or x <= -(1 << y):
        return 0
    if x == 0 or y == 0:
        return 1
    if x & 1:
        mem[(x, y)] = solve(x + 1 >> 1, y - 1) + solve(x - 1 >> 1, y - 1)
    else:
        mem[(x, y)] = solve(x >> 1, y - 1)
    return mem[(x, y)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(solve(x, y))