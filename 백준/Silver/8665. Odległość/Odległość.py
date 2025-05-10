input()
ans, val = 0, 0
for a in map(int, input().split()):
    val = max(val + 1, a)
    ans = max(ans, val + a)
print(ans)