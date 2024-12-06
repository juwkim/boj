n = int(input())
ans = n
for i, h in enumerate(sorted(map(int, input().split())), 1):
    ans = min(ans, h + n - i)
print(ans)