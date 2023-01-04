def g(): return [*map(int, input().split())]

N = int(input())
nums = sorted(g() for _ in range(N))
ans = 0
for i in range(N - 1):
    t1, x1 = nums[i]
    t2, x2 = nums[i + 1]
    ans = max(ans, abs(x2 - x1) / (t2 - t1))
print(ans)