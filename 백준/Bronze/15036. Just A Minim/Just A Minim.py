input()
nums=[*map(int,input().split())]
print(2*nums.count(0)+sum([1/i for i in filter(lambda x: x>0, nums)]))