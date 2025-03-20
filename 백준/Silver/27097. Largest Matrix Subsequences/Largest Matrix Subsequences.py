R, C, *nums = map(int, open(0).read().split())
a = [nums[i:i+C] for i in range(0, R*C, C)]
px1 = [[0] * C for _ in range(R + 1)]
for i in range(1, R + 1):
    cur = 0
    for j in range(1, C):
        cur += a[i-1][j-1] >= a[i-1][j]
        px1[i][j] = cur + px1[i-1][j]
px2 = [[0] * (C + 1) for _ in range(R)]
for j in range(1, C + 1):
    cur = 0
    for i in range(1, R):
        cur += a[i-1][j-1] >= a[i][j-1]
        px2[i][j] = cur + px2[i][j-1]
ans, Max = [], 1
for i in range(R):
    for j in range(C):
        for k in range((Max + C - j - 1) // (C - j), R - i + 1):
            for l in range((Max + k - 1) // k, C - j + 1):
                def solve():
                    if px1[i+k][j+l-1] - px1[i+k][j] - px1[i][j+l-1] + px1[i][j]:
                        return False
                    if px2[i+k-1][j+l] - px2[i][j+l] - px2[i+k-1][j] + px2[i][j]:
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