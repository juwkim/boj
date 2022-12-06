N = int(input())
nums = [input().split() for _ in range(N)]
captain_idx, captain_num = 0, 0
for i in range(N):
    count = sum(any(nums[i][k] == nums[j][k] for k in range(5)) for j in range(N))
    if count > captain_num:
        captain_num = count
        captain_idx = i
print(captain_idx+1)