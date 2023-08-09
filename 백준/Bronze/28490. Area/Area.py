ans = 0
for _ in range(int(input())):
    h, w = map(int, input().split())
    ans = max(ans, h * w)
print(ans)