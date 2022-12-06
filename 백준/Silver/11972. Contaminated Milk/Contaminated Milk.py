g = lambda: [*map(int, input().split())]

N, M, D, S = g()

nums = [[] for _ in range(N)]
for _ in range(D):
    idx, *l = g()
    nums[idx-1].append(l)


contaminated = set(range(1, M+1))
for _ in range(S):
    idx, t = g()
    idx -= 1
    res = set()
    for milk, time in nums[idx]:
        if time < t:
            res.add(milk)
    contaminated &= res
    
ans = 0
bad = contaminated.pop()
for eat in nums:
    for milk, time in eat:
        if milk == bad:
            ans += 1
            break
print(ans)