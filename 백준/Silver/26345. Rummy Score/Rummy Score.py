for _ in range(int(input())):
    a = [*map(int, input().split())]
    print("Rummy Hand:", *a)
    a.sort()
    ans, nums = 1e9, []
    def solve(idx):
        global ans
        if idx == 7:
            ans = min(ans, sum(sum(l) for l in nums if len(l) < 3))
            return
        for l in nums:
            if (len(l) == 1 or l[0] != l[-1]) and l[-1] + 1 == a[idx] or l[0] == l[-1] == a[idx]:
                l.append(a[idx])
                solve(idx + 1)
                l.pop()
        nums.append([a[idx]])
        solve(idx + 1)
        nums.pop()
    solve(0)
    print(ans)
    print()