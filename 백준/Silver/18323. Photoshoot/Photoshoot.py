g = lambda: [*map(int, input().split())]
N = int(input())
nums = g()
for i in range(1, nums[0]):
    check = set(range(1, N+1))
    ans = []
    num = i
    idx = 0
    while num in check:
        ans.append(num)
        check.remove(num)
        if len(ans) == N:
            break
        num = nums[idx] - num
        idx += 1
    if len(ans) == N:
        break
print(*ans)