import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
names = input().split()
table = names[:4]
dq = deque(names[4:])

def get_team(side):
    if side == 'W':
        return table[0], table[2]
    return table[1], table[3]

dynasties = []
cur_side = None
cur_len = 0
cur_team = None

for s in input():
    team = get_team(s)
    if cur_side == s:
        cur_len += 1
    else:
        if cur_len:
            dynasties.append((cur_len, cur_team))
        cur_side = s
        cur_len = 1
        cur_team = team
        if dynasties:
            cur_team = cur_team[::-1]

    if s == 'W':
        table[0], table[2] = table[2], table[0]
        leave = table[3]
        table[3] = table[1]
        table[1] = dq.popleft()
        dq.append(leave)
    else:
        table[1], table[3] = table[3], table[1]
        leave = table[2]
        table[2] = table[0]
        table[0] = dq.popleft()
        dq.append(leave)

dynasties.append((cur_len, cur_team))
maxlen = max(length for length, _ in dynasties)
for length, team in dynasties:
    if length == maxlen:
        print(*team)