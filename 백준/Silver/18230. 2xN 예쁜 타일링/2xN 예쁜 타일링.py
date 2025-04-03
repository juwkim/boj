g = lambda: map(int, input().split())

N, A, B = g()
S, T = sorted(g()), sorted(g())
ans = 0
while N:
    if N == 1:
        ans += S.pop()
        N -= 1
    elif T and (len(S) < 2 or S[-1] + S[-2] < T[-1]):
        ans += T.pop()
        N -= 2
    else:
        ans += S.pop()
        N -= 1
print(ans)