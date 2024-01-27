import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
s = input()
ans = [bytearray(n) for _ in range(n)]
idx = 0
def solve(i, j, l):
    global idx
    if s[idx] == 'Q':
        l >>= 1
        idx += 1
        solve(i, j, l)
        solve(i, j + l, l)
        solve(i + l, j, l)
        solve(i + l, j + l, l)
    else:
        for x in range(i, i + l):
            for y in range(j, j + l):
                ans[x][y] = (s[idx] == 'B')
        idx += 1
solve(0, 0, n)
print(f"#define quadtree_width {n}")
print(f"#define quadtree_height {n}")
print("static char quadtree_bits[] = {")
for i in range(n):
    for j in range(0, n, 8):
        num, w = 0, 1
        for k in range(8):
            num += ans[i][j + k] * w
            w <<= 1
        print(f"0x{num:02x},", end='')
    print()
print("};")