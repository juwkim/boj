g = lambda: [*map(int, input().split())]

n, m, a = g()
nums = g()

cnt = 0
for i in range((n - 1) * m):
    cnt += 2 * nums[i] < nums[i + m]
print(a * cnt)