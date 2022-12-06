n = int(input())
nums = [int(input()) for _ in range(n)]

s_nums = sorted(nums, reverse=True)

dic = {}
for i in range(n):
    if dic.get(s_nums[i]) == None:
        dic[s_nums[i]] = i
for i in range(n):
    print(dic[nums[i]] + 1)