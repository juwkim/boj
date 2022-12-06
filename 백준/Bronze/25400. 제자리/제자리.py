g = lambda: [*map(int, input().split())]
N = int(input())
ans = 0
cur = 1
for num in g():
    if num == cur:
        cur += 1
    else:
        ans += 1
print(ans)