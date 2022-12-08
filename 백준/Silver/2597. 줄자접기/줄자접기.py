g = lambda: [*map(int, input().split())]
N = int(input())
p = [sorted(g()) for _ in range(3)]
for i in range(3):
    if p[i][0] == p[i][1]:
        continue    
    mid = sum(p[i]) / 2
    if 2 * mid < N:
        for j in range(i + 1, 3):
            p[j][0] = abs(mid - p[j][0])
            p[j][1] = abs(mid - p[j][1])
            p[j].sort()
        N = N - mid
    else:
        for j in range(i + 1, 3):
            if mid < p[j][0]:
                p[j][0] = 2 * mid - p[j][0]
            if mid < p[j][1]:
                p[j][1] = 2 * mid - p[j][1]
            p[j].sort()
        N = mid
print(f"{N:#.1f}")