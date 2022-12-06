N = int(input())
nums = []
p = N // 3
for i in range(p):
    nums.append([3*i+1, 3*i+2, 3*i+3])

ans = {*range(1, N+1)}

for _ in range(int(input())):
    s = input()[0]
    a, b, c = map(set, zip(*nums))
    if s == 'f':
        ans &= a
    elif s == 's':
        ans &= b
    else:
        ans &= c
    nums = sum(map(list, zip(*nums)), [])
    tmp = [[] for _ in range(p)]
    idx = 0
    for i in range(p):
        for j in range(3):
            tmp[i].append(nums[idx])
            idx += 1
    nums = tmp
print(*ans)