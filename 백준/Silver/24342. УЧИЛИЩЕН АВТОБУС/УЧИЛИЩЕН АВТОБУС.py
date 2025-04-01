import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
buf = [g() for _ in range(N)]
left_time, cur_time = sum(x[0] for x in buf), 0
nums = []
for t, k, *l in buf:
    nums.extend(max(cur_time, num) + left_time for num in l)
    cur_time += t
    left_time -= t
print(sorted(nums)[min(len(nums), M) - 1])