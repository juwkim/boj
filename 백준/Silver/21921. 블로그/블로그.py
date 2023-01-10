from collections import Counter

N, X = map(int, input().split())
nums = [*map(int, input().split())]
cnt = Counter([cur:= sum(nums[:X])])
for i in range(X, N):
    cur += nums[i] - nums[i - X]
    cnt[cur] += 1

key = max(cnt)
if key == 0:
    print('SAD')
else:
    print(key)
    print(cnt[key])