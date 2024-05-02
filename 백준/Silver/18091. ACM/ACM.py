import sys
input = lambda: sys.stdin.readline().rstrip()

def time(states):
    accepted, cur = 0, 0
    for state in states:
        if state[0] == '-':
            continue
        accepted += 1
        p, t = state.split('/')
        h, m, s = map(int, t.split(':'))
        cur += 1200 * (int(p[1]) - 1) + 3600 * h + 60 * m + s
    return accepted, cur

N, M = map(int, input().split())
score = []
for _ in range(N):
    name, *states = input().split()
    if name == "NijeZivotJedanACM":
        continue
    score.append((*time(states), name))
name, *states = input().split()
accepted, cur = time(states)
score.append((accepted, cur, name))
score.sort(key=lambda x: (-x[0], x[1], x[2]))
ans = score.index((accepted, cur, name)) + 1
print(ans)