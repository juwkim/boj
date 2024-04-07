n, *a = map(int, open(0).read().split())
ans = [[] for _ in range(n)]
num = 1
E = 0
for i, x in sorted(enumerate(a), key=lambda x: -x[1]):
    E += 2 * num + x - 1
    for _ in range(x):
        ans[i].append(num)
        num += 1
print("%.5f" % (E / 2))
for l in ans:
    print(*l)