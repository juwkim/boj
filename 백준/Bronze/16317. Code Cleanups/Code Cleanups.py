g = lambda: [*map(int, input().split())]

n = int(input())
cnt = 0
nums = g()
buf = [nums[0]]
for i in range(1, n):
    if nums[i] * len(buf) - sum(buf) >= 20:
        buf = [nums[i]]
        cnt += 1
    else:
        buf.append(nums[i])

print(cnt + bool(buf))