g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()


check = set()
def dfs(idx, Sum):

    if idx == n:
        return
    
    check.add(Sum + nums[idx])
    dfs(idx + 1, Sum)
    dfs(idx + 1, Sum + nums[idx])


dfs(0, 0)
num = 1
while num in check:
    num += 1
print(num)