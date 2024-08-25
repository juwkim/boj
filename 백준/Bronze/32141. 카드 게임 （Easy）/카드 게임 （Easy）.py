N, H = map(int, input().split())
ans = 0
for d in map(int, input().split()):
    ans += 1
    H -= d
    if H <= 0:
        break
else:
    ans = -1
print(ans)