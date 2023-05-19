from collections import defaultdict

ans = {}
product = set()
for _ in range(int(input())):
    q, s, v = map(int, input().split())
    if s not in ans:
        ans[s] = defaultdict(int)
    ans[s][q] += v
    product.add(q)

product = sorted(product)
print(-1, *product)
for s in sorted(ans.keys()):
    print(s, *[ans[s][p] for p in product])