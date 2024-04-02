from collections import defaultdict

dic = defaultdict(lambda: defaultdict(int))
for _ in range(int(input())):
    name, task, score = input().split()
    dic[name][task] = max(dic[name][task], int(score))
for score, name in sorted((-sum(v.values()), name) for name, v in dic.items()):
    print(name, -score)