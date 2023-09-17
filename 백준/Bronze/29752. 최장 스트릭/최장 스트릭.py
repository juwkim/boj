N = int(input())
ans, cur = 0, 0
for num in input().split():
    if num == '0':
        ans = max(ans, cur)
        cur = 0
    else:
        cur += 1
ans = max(ans, cur)
print(ans)