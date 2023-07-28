g = lambda: [*map(int, input().split())]

C = int(input())
lines = [[0] * (C + 1)] + [[0] + g() for _ in range(2)]
ans = 0
for i in range(1, 3):
    for j in range(1, C + 1):
        if lines[i][j] == 0:
            continue
        if i + j & 1:
            if lines[i][j - 1] and lines[i - 1][j]:
                ans -= 1
            elif lines[i][j - 1] or lines[i - 1][j]:
                ans += 1
            else:
                ans += 3
        else:
            if lines[i][j - 1]:
                ans += 1
            else:
                ans += 3
print(ans)