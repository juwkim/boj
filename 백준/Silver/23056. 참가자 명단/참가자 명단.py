g = lambda: [*map(int, input().split())]

N, M = g()
buf = [[] for _ in range(N + 1)]
while (s:= input()) != '0 0':
    team, name = s.split()
    team = int(team)
    if len(buf[team]) < M:
        buf[team].append(name)

for i in range(1, N, 2):
    buf[i].sort(key=lambda x: (len(x), x))
    for name in buf[i]:
        print(i, name)

for i in range(2, N + 1, 2):
    buf[i].sort(key=lambda x: (len(x), x))
    for name in buf[i]:
        print(i, name)