g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    n, m, c = g()
    nums = g()
    ans = 0
    for i in range(n + 1 - m):
        s = nums[i:i + m]
        if max(s) - min(s) <= c:
            ans += 1
    print(ans)