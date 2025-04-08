input()
ans = 1e9
for i, c in enumerate(sorted(map(int, input().split())), 1):
    ans = min(ans, c // i)
print(ans)