g = lambda: [*map(int, input().split())]

N, L, K = g()
nums = sorted([int(input()) for _ in range(N)])

ans = 0
for num in nums:
    if num <= L:
        ans += 1
        L += K
print(ans)