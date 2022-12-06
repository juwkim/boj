from collections import defaultdict
res = defaultdict(dict)
# cnt, time
for _ in range(int(input())):
    time, team, problem, state = input().split()
    if team not in res[problem]:
        res[problem][team] = [0, 0]
    if res[problem][team][1] == 0:
        res[problem][team][0] += 1
        if state == 'A':
            res[problem][team][1] = int(time)
for problem in 'ABCDEFGHI':
    solved_cnt, submission_cnt, total_time = 0, 0, 0
    for cnt, time in res[problem].values():
        if time:
            solved_cnt += 1
            submission_cnt += cnt
            total_time += time
    if solved_cnt:
        avg_cnt = submission_cnt / solved_cnt
        avg_time = total_time / solved_cnt
        print(f'{problem} {solved_cnt} {avg_cnt:#.2f} {avg_time:#.2f}')
    else:
        print(f'{problem} {solved_cnt}')