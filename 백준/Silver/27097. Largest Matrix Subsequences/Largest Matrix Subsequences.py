R, C, *nums = map(int, open(0).read().split())
ans, Max = [], 1
a = [nums[i:i+C] for i in range(0, R*C, C)]
px = [[0] * C for _ in range(R + 1)]
for i in range(1, R + 1):
    cur = 0
    for j in range(1, C):
        cur += a[i-1][j-1] >= a[i-1][j]
        px[i][j] = cur + px[i-1][j]

# for l in px:
#     print(*l)
# print()
        
for i in range(R):
    for j in range(C):
        for k in range((Max + C - j - 1) // (C - j), R - i + 1):
            for l in range((Max + k - 1) // k, C - j + 1):
                def solve():
                    if px[i+k][j+l-1] - px[i+k][j] - px[i][j+l-1] + px[i][j]:
                        return False
                    for s in range(i, i + k - 1):
                        for t in range(j, j + l):
                            if a[s][t] >= a[s+1][t]:
                                return False
                    return True
                if solve():
                    if k * l > Max:
                        ans = [(i + 1, j + 1, k, l)]
                        Max = k * l
                    else:
                        ans.append((i + 1, j + 1, k, l))
for row in ans:
    print(*row)