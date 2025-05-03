import sys
input = sys.stdin.readline

(cur_start, cur_end), *nums = sorted([*map(int, input().split())] for _ in range(int(input())))
for start, end in nums:
    if start <= cur_end:
        cur_end = max(cur_end, end)
    else:
        print(cur_start, cur_end)
        cur_start, cur_end = start, end
print(cur_start, cur_end)