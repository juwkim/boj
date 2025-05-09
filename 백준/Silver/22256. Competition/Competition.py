g = lambda: map(int, input().split())

n, a, b = g()
nums = sorted(zip(g(), g()), key=lambda x: x[1] - x[0])
print(sum(nums[i][0] for i in range(a)) + sum(nums[i][1] for i in range(a, n)))