def g(): return [*map(int, input().split())]

while sum(l := g()):
    n, r = l
    nums = [*range(n, 0, -1)]
    for _ in range(r):
        p, c = g()
        p -= 1        
        nums = nums[p:p+c] + nums[:p] + nums[p+c:]
    print(nums[0])