import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

k, r = g()
amounts = g()
ans = 0
for _ in range(r):
    *ingre, cost = g()
    val = cost * min(i // j for i, j in zip(amounts, ingre) if j)
    ans = max(ans, val) 
print(ans)