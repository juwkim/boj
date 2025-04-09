import sys
input = sys.stdin.readline
from collections import defaultdict

T, N = map(int, input().split())
bad_logs, bad_players = [], set()
pos = [1] * (N + 1)
item = [defaultdict(int) for _ in range(N + 1)]
for _ in range(T):
    i, player, code, arg1, *arg2 = input().split()
    i, player, arg1 = map(int, (i, player, arg1))
    match code:
        case 'M':
            pos[player] = arg1
        case 'F':
            if arg1 != pos[player]:
                bad_logs.append(i)
            item[player][arg1] += 1
        case 'C':
            arg2 = int(arg2[0])
            if item[player][arg1] == 0 or item[player][arg2] == 0:
                bad_logs.append(i)
            item[player][arg1] = max(0, item[player][arg1] - 1)
            item[player][arg2] = max(0, item[player][arg2] - 1)
        case 'A':
            if pos[player] != pos[arg1]:
                bad_logs.append(i)
                bad_players.add(player)
print(len(bad_logs))
if bad_logs:
    print(*bad_logs)
print(len(bad_players))
if bad_players:
    print(*sorted(bad_players))