def solve(i, l):
    global ans
    if i == n:
        if m not in l:
            return
        a, b = 1, 1
        cur = 0
        for num in l:
            for _ in range(num):
                a = (a * (5, 11)[cur]) % mod
                b = (b * (11, 5)[cur]) % mod
                cur ^= 1
            cur ^= 1
        ans = (ans + a + b) % mod
        return        
    for j in range(1, min(n - i, m) + 1):
        solve(i + j, l + [j])

mod = 1000000007
n, m = map(int, input().split())
ans = 0
solve(0, [])
print(ans)