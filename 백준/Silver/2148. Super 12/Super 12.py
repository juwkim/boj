import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

teams = []
state = defaultdict(lambda: {'pts': 0, 'score': 0, 'conceded': 0, 'tries': 0, 'conceded_tries': 0, 'games': 0})
while (team:=input()) != '#':
    teams.append(team)
round_no = 1
while (line:=input()) != '#':
    h, a, *l = line.split()
    sh, sa, th, ta = map(int, l)
    for k, s, c, t, ct in (h, sh, sa, th, ta), (a, sa, sh, ta, th):
        state[k]['score'] += s
        state[k]['conceded'] += c
        state[k]['tries'] += t
        state[k]['conceded_tries'] += ct
        state[k]['games'] += 1
    if sh > sa:
        state[h]['pts'] += 4
    elif sh < sa:
        state[a]['pts'] += 4
    else:
        state[h]['pts'] += 2
        state[a]['pts'] += 2
    if th >= 4: state[h]['pts'] += 1
    if ta >= 4: state[a]['pts'] += 1
    if sh < sa and sa - sh < 8: state[h]['pts'] += 1
    if sa < sh and sh - sa < 8: state[a]['pts'] += 1
    if all(state[t]['games'] == state[teams[0]]['games'] for t in teams):
        print(f"Round {round_no}")
        for t in sorted(teams, key=lambda t: (-state[t]['pts'], -(state[t]['score'] - state[t]['conceded']), -state[t]['tries'])):
            print(f"{t:<21}{state[t]['pts']:>2}{state[t]['score']:>4}{state[t]['conceded']:>4}{state[t]['tries']:>3}{state[t]['conceded_tries']:>3}")
        print()
        round_no += 1