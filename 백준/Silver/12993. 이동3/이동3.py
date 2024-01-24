x, y = map(int, input().split())
ans = 1
while x or y:
    x, r1 = divmod(x, 3)
    y, r2 = divmod(y, 3)
    if r1 + r2 != 1:
        ans = 0
        break  
print(ans)