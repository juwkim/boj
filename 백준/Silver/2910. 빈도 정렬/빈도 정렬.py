g = lambda: map(int, input().split())
N, C = g()
cnt, idx = {}, {}
for i, num in enumerate(g()):
    if cnt.get(num):
        cnt[num] += 1
    else:
        cnt[num] = 1
        idx[num] = i
for k, v in sorted(cnt.items(), key=lambda x: (-x[1], idx[x[0]])):
    print(*[k for _ in range(v)], end=' ')