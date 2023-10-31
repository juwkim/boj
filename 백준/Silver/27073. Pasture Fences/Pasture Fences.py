import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
px = [0]
for _ in range(N):
    px.append(px[-1] + int(input()))

s, t, cur = -1, -1, float('inf')
for i in range(N, 0, -1):
    for j in range(i, N + 1):
        if abs(px[j] - px[j - i]) < cur:
            s, t = j - i + 1, j
            cur = abs(px[j] - px[j - i])
print(s, t, cur)