g = lambda: [*map(int, input().split())]

n = int(input())
ans = 1e9
for idx, num in enumerate(sorted(g()), 1):
    if num > idx:
        ans = 'impossible'
        break
    ans = min(ans, num / idx)
print(ans)