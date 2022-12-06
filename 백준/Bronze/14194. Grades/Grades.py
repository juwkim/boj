g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n = int(input())
    nums = sorted(g())
    a = (nums[0] + nums[-1]) / 2
    b = sum(nums) / n
    print('Yes' if abs(a - b) < 1 else 'No')