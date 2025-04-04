input()
ans, cur = 0, 0
for A in map(int, input().split()):
    ans = max(ans, cur:=min(cur + 1, A))
print(ans)