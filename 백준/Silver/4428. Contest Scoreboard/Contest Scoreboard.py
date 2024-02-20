from collections import defaultdict

dic = defaultdict(lambda: defaultdict(lambda: [0, 0]))
for s in open(0):
    *a, l = s.split()
    c, p, t = map(int, a)
    if dic[c][p][0]:
        continue
    if l == 'C':
        dic[c][p][0] = t
    elif l == 'I':
        dic[c][p][1] += 20
res = []
for k, v in dic.items():
    correct = 0
    time = 0
    for t, penalty in v.values():
        if not t:
            continue
        correct += 1
        time += t + penalty
    res.append([k, correct, time])
for c, p, t in sorted(res, key=lambda x: (-x[1], x[2], x[0])):
    print(c, p, t)