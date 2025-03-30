n, k = map(int, input().split())
prv, cnt = [5] * k, k // 2 + 1
print(*prv)
for _ in range(n - 1):
    l = [0] * k
    for idx in sorted(range(k), key=lambda x: prv[x])[:cnt]:
        l[idx] = prv[idx] + 1
    print(*l)
    prv = l