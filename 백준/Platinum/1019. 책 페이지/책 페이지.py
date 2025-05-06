def solve(prefix, num):
    c, *s = str(num)
    c, l = int(c), len(s)
    if l:
        for i in range(10):
            cnt[i] += c * l * 10 ** (l - 1)
    for i in range(1, c):
        cnt[i] += 10 ** l
    if prefix:
        for c in prefix:
            cnt[int(c)] += num

cnt = [0] * 10
N, prefix = input(), ''
for c in N:
    cnt[int(c)] += 1

for i in range(len(N)):
    solve(prefix, int(N[i]) * 10 ** (len(N) - i - 1))
    prefix += N[i]

p = len(N) * (int(N) + 1 - 10 ** (len(N) - 1))
for i in range(1, len(N)):
    p += i * 9 * 10 ** (i - 1)
cnt[0] = p - sum(cnt[1:])
print(*cnt)