n = int(input())
nums = [*map(int, input().split())]
t, s = 0, 0
cnt = 0
for i in range(n):
    t += i + 1
    s += nums[i]
    cnt += (t == s)
print(cnt)