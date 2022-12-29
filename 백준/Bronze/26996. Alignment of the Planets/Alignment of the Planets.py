g = lambda: tuple(map(int, input().split()))

from itertools import combinations
N = int(input())
cows = {g(): i for i in range(1, N + 1)}
ans = 0
ans_buf = []
for a, b, c in combinations(cows, 3):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
        ans += 1
        ans_buf.append((cows[a], cows[b], cows[c]))
print(ans)
for line in ans_buf:
    print(*line)