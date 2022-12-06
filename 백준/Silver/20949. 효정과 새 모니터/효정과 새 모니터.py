g = lambda: [*map(int, input().split())]

N = int(input())
nums = [g() + [idx + 1] for idx in range(N)]
nums.sort(key=lambda x: (-(x[0]**2 + x[1]**2), x[2]))
for _ in range(N):
    print(nums[_][2])