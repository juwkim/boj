import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, m, d = g()
nums = sorted([g() for _ in range(m)] + [[d, 0]])
stops, idx = 0, 0
pos, tank = 0, n * 10
while pos < d and tank < d - pos:    
    max_reach, best_idx = -1, -1    
    while idx < m and nums[idx][0] <= pos + tank:
        max_reach, best_idx = nums[idx][0], idx
        idx += 1
    if best_idx == -1:
        stops = -1
        break
    stops += 1
    pos, tank = nums[best_idx][0], n * 10
print(stops)