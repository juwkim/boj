import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    m = int(input())
    nums = [[*map(int, input().split())] for _ in range(m)]
    ans = 0
    pre_day, pre_time = 0, 0
    for d, s, e in sorted(nums, key=lambda x: (x[0], x[2])):
        if d > pre_day or s >= pre_time:
            ans += 1
            pre_day, pre_time = d, e
    print(f"Scenario #{tc}:\n{ans}\n")