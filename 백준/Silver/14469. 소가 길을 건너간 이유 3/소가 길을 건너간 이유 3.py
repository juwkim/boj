g = lambda: [*map(int, input().split())]

ans = 0
for time, due in sorted(g() for _ in range(int(input()))):
    ans = max(ans, time) + due
print(ans)