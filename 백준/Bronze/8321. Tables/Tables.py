g = lambda: [*map(int, input().split())]

n, k, s = g()
nums = sorted(g(), reverse=True)
cnt = k * s
for i in range(n):
    cnt -= nums[i]
    if cnt <= 0:
        print(i + 1)
        break