from itertools import combinations

P = [[*map(int, input().split())] for _ in range(int(input()))]
ans = 0
for (x1, y1), (x2, y2), (x3, y3) in combinations(P, 3):
    ans = max(ans, abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)
print(ans)