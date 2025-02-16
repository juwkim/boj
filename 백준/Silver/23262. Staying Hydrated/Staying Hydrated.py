import sys
input = sys.stdin.readline
check = lambda p, nums: sum(max(0, x[0] - p, p - x[1]) for x in nums)

def solve(nums):
    nums.sort()
    lo, hi = nums[0][0], max(p[1] for p in nums)
    while hi > lo + 2:
        p1 = lo + (hi - lo) // 3
        p2 = hi - (hi - lo) // 3
        if check(p1, nums) > check(p2, nums):
            lo = p1
        else:
            hi = p2
    return min(range(lo, hi + 1), key=lambda x: check(x, nums))

for tc in range(1, 1 + int(input())):
    xs, ys = [], []
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        xs.append((x1, x2))
        ys.append((y1, y2))
    print(f"Case #{tc}: {solve(xs)} {solve(ys)}")