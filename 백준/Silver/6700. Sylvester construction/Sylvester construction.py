import sys
input = sys.stdin.readline

def solve(d, x, y):
    if d == 1:
        return 1
    l = d >> 1
    num = solve(l, x % l, y % l)
    if x < l or y < l:
        return num
    return -num

for _ in range(int(input())):
    n, x, y, w, h = map(int, input().split())
    for i in range(y, y + h):
        for j in range(x, x + w):
            print(solve(n, i, j), end=' ')
        print()
    print()