g = lambda: [*map(int, input().split())]
N, S, M = map(int, input().split())
V = g()
l = set([S])
for i in range(N):
    if not l:
        break
    nums = set()
    for num in l:
        for p in (num + V[i], num - V[i]):
            if 0 <= p <= M:
                nums.add(p)
    l = nums

if l:
    print(max(l))
else:
    print(-1)