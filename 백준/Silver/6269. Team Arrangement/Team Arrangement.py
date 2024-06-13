from collections import defaultdict

l = open(0).read().split()
i = 0
while l[i] != '0':
    team = defaultdict(list)
    for _ in range(22):
        num, name, role = int(l[i]), l[i + 1], l[i + 2]; i += 3
        record = 0
        while l[i].count('-') == 1:
            a, b = map(int, l[i].split('-')); i += 1
            record += b - a + 1
        team[role].append((num, record, name, role))
    a, b, c = map(int, l[i].split('-')); i += 1
    if len(team['G']) < 1 or len(team['D']) < a or len(team['M']) < b or len(team['S']) < c:
        print('IMPOSSIBLE TO ARRANGE')
    else:
        G = sorted(team['G'])[:1]
        D = sorted(team['D'])[:a]
        M = sorted(team['M'])[:b]
        S = sorted(team['S'])[:c]
        ans = G + D + M + S
        cap = max(range(len(ans)), key=lambda x: (ans[x][1], ans[x][0]))
        ans.insert(0, ans.pop(cap))
        for num, _, name, role in ans:
            print(num, name, role)
    print()