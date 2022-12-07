g = lambda: [*map(int, input().split())]
n, m, q = g()
buf = [[[0, -1] for _ in range(m + 1)] for _ in range(n + 1)]
for _ in range(q):
    *l, result = input().split()
    time, team, problem = map(int, l)
    if buf[team][problem][1] == -1:
        if result == 'AC':
            buf[team][problem][1] = time
        else:
            buf[team][problem][0] += 1

res = []
for team in range(1, n + 1):
    t_cnt, t_time = 0, 0
    for cnt, time in buf[team][1:]:
        if time != -1:
            t_cnt += 1
            t_time += time + 20 * cnt
    res.append((t_cnt, t_time, team))
res.sort(key=lambda x: (-x[0], x[1], x[2]))
for cnt, time, team in res:
    print(team, cnt, time)