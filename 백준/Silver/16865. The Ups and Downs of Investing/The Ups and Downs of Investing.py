g = lambda: [*map(int, input().split())]


S, N, M = g()
res = []
nums = []
while len(nums) != S:
    nums += g()
cur = 0
for i in range(S-1):
    if cur == 0:
        if nums[i] > nums[i+1]:
            cur -= 2
        else:
            cur += 2
    elif cur > 0:
        if nums[i] > nums[i+1]:
            res.append(cur)
            cur = -2
        else:
            cur += 1
    else:
        if nums[i] < nums[i+1]:
            res.append(cur)
            cur = 2
        else:
            cur -= 1 
res.append(cur)


u, d = 0, 0
for i in range(len(res)-1):
    a, b = res[i], res[i+1]
    if a >= N and -b >= N:
        u += 1
    elif -a >= M and b >= M:
        d += 1
print(u, d)