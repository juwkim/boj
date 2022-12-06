g = lambda: [*map(int, input().split())]

N, M = g()
ans = 0
for num in g():    
    cur = num
    while M % (cur + 1) == 0:
        cur += 1
    ans += cur - num
print(ans)