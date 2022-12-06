g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    input()
    ans = None
    cur = None
    
    for num in g():
        if cur == None:
            if ans:
                ans = max(ans, num)
            else:
                ans = num
            if num > 0:
                cur = num
        elif cur + num > 0:
            cur += num
            ans = max(ans, cur)
        else:
            cur = None
    print(ans)