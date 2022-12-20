g = lambda: list(map(int, input().split()))

N, M , P = g()
dic = {name: [[0, 0, ''] for _ in range(N + 1)] for name in input().split()}
for _ in range(P):
    problem, time, name, res = input().split()
    h, m = map(int, time.split(':'))
    time = h * 60 + m
    problem = int(problem)
    if res == 'solve':
        if dic[name][problem][2] == 'wrong':
            dic[name][problem][1] = time - dic[name][problem][1]
            dic[name][problem][2] = 'solve'
        elif dic[name][problem][2] == 'solve':
            continue
        else:
            dic[name][problem][2] = 'one'
    elif dic[name][problem][2] == '':
        dic[name][problem][1] = time
        dic[name][problem][2] = 'wrong'
    
score = {name: 0 for name in dic}
for problem in range(1, N + 1):
    solved = []
    for name in dic:
        if dic[name][problem][2] == 'solve':
            solved.append((dic[name][problem][1], name))
        elif dic[name][problem][2] == 'wrong':
            score[name] += M
        else:
            score[name] += M + 1
    solved.sort()
    for i in range(len(solved)):
        score[solved[i][1]] += i + 1
for name, val in sorted(score.items(), key=lambda x: (x[1], x[0])):
    print(name)