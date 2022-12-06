g = lambda: [*map(int, input().split())]

N = int(input())
ans = 0
res = set()
for num in g():
    if num in res:
        ans = max(ans, len(res))
        res.remove(num)
    else:
        res.add(num)
print(max(ans, len(res)))