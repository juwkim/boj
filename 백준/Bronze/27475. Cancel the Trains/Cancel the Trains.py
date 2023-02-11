def g(): return [*map(int, input().split())]

for _ in range(int(input())):
    n, m = g()
    nums = set(g())
    ans = 0
    for num in g():
        ans += num in nums
    print(ans)