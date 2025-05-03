from math import factorial as f

N, S, E = map(int, input().split())
expressions = []
for _ in range(E):
    l = []
    for e in input().split('+'):
        W, R = map(int, e.split('x'))
        l.append((W, R))
    expressions.append(l)

ans = 0
cnt = [0] * (S + 1)
def solve(i, num):
    global ans
    if i == N:
        if any(all(cnt[R] >= W for W, R in exp) for exp in expressions):
            num = f(N)
            for j in range(1, S + 1):
                num //= f(cnt[j])
            ans += num
        return
    for j in range(num, S + 1):
        cnt[j] += 1
        solve(i + 1, j)
        cnt[j] -= 1
solve(0, 1)
print(ans)