ans, cur = 0, None
for _ in range(int(input())):
    num = float(input())
    if cur == None:
        ans = max(ans, num)
        if num > 1:
            cur = num
    elif cur * num > 1:
        cur *= num
        ans = max(ans, cur)
    else:
        cur = None
print("%.3f" % ans)