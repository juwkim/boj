ans = 0
for _ in range(int(input())):
    a, b, *l = map(int, input().split())
    l.sort()
    ans = max(ans, max(a, b) + l[3] + l[4])
print(ans)