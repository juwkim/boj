N = int(input())
ans, cur = 0, 1
while N >= cur * cur:
    ans += 1
    N -= cur * cur
    cur += 2
print(ans)