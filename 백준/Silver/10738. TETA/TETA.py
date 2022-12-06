g = lambda: [*map(int, input().split())]


from collections import Counter
K = int(input())
costs = g()
X = int(input())
big = Counter(g())
T = int(input())

nums = Counter(g())            

ans = 1e10
add = 0
while True:
    tmp = add + sum(costs[num-1] * nums[num] for num in nums)
    ans = min(ans, tmp)
    add += X
    
    left = nums - big
    if left == nums:
        break
    nums = left
    
print(ans)