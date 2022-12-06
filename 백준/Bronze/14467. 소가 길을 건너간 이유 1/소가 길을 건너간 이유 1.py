buf = [-1] * 11
cnt = 0
a = set()
for _ in range(int(input())):
    N, M = map(int, input().split())
    a.add(N)
    if buf[N] != M:
        cnt += 1
        buf[N] = M
print(cnt - len(a))