import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M, P = g()
ans = 1
for _ in range(N):
    item, nums = 0, []
    for num in g():
        if num == -1:
            item += 1
        else:
            nums.append(num)
    nums.sort()
    for num in nums:
        while P < num and item:
            P <<= 1
            item -= 1
        if P < num:
            ans = 0
            break
        P += num
    if ans == 0:
        break
    P <<= item
print(ans)