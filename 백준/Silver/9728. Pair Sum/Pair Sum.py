g = lambda: [*map(int, input().split())]

for step in range(1, 1 + int(input())):
    N, M = g()
    nums = g()
    ans = set()
    l, r = 0, N - 1
    while l < r:
        a, b = nums[l], nums[r]
        if a + b == M:
            ans.add((a, b))
            l += 1
            r -= 1
        elif a + b < M:
            l += 1
        else:
            r -= 1
    print(f'Case #{step}: {len(ans)}')