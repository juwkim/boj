import sys
g = lambda: map(int, sys.stdin.readline().split())

N, S = g()
total_cost, min_cost = 0, 5000
for _ in range(N):
    C, Y = g()
    min_cost = min(min_cost + S, C)
    total_cost += min_cost * Y
print(total_cost)