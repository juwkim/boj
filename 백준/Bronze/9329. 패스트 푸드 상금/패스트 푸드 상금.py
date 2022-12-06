g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    n, m = g()
    
    buf = [g() for _ in range(n)]
    sticker = g()
    
    ans = 0
    for change in buf:
        K, *l, money = change
        cnt = min(sticker[i-1] for i in l)
        ans += cnt * money
    print(ans)