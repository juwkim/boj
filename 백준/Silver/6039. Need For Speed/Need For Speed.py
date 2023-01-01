def g(): return [*map(int, input().split())]

F, M, N = g()
ans = []
p, q = F, M
for f, m, idx in sorted([g() + [i + 1] for i in range(N)], key=lambda x: x[1] / x[0]):

    if (p + f) * q <= p * (q + m):
        break
    p += f
    q += m
    ans.append(idx)
if ans:
    print(*sorted(ans))
else:
    print('NONE')