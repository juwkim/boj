tc = 1
for s in map(str.rstrip, [*open(0)][:-1]):
    n = len(s)
    ans = 0
    def dfs(i, prev):
        global ans
        if i == n:
            ans += 1
            return
        cur = 0
        for j in range(i, n):
            cur += int(s[j])
            if cur >= prev:
                dfs(j + 1, cur)
    dfs(0, 0)
    print(f"{tc}. {ans}")
    tc += 1