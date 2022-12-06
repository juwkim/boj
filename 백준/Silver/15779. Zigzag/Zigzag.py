g = lambda: [*map(int, input().split())]

N = int(input())

nums = g()
tmp = [(nums[i] > nums[i+1]) - (nums[i] < nums[i+1]) for i in range(N-1)]
ans = 2
cnt = 2
for i in range(len(tmp)-1):
    if tmp[i] and tmp[i] + tmp[i+1] == 0:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 2
ans = max(ans, cnt)
print(ans)