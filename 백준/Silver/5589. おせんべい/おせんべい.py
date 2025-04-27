import sys
g = lambda: map(int, sys.stdin.readline().split())

R, C = g()
col_mask = [0] * C
for i in range(R):
    for j, a in enumerate(g()):
        if a:
            col_mask[j] |= 1 << i
ans = 0
for r_mask in range(1 << R):
    cur = 0
    for m in col_mask:
        diff = (m ^ r_mask).bit_count()
        cur += max(diff, R - diff)
    ans = max(ans, cur)
print(ans)