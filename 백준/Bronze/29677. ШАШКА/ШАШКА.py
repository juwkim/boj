scores = {}
for _ in range(int(input())):
    score, name = input().split()
    scores[name] = int(score)

for _ in range(int(input())):
    p1, p2, res = input().split()
    res = int(res)
    
    if res == 0:
        sp1, sp2 = 0.5, 0.5
    elif res == 1:
        sp1, sp2 = 1, 0
    elif res == 2:
        sp1, sp2 = 0, 1
    
    dp1 = 15 * (sp1 - 1 / (1 + pow(10, (scores[p2] - scores[p1]) / 400)))
    dp2 = 15 * (sp2 - 1 / (1 + pow(10, (scores[p1] - scores[p2]) / 400)))

    scores[p1] = max(int(scores[p1] + dp1), 0)
    scores[p2] = max(int(scores[p2] + dp2), 0)

for name, score in sorted(scores.items(), key=lambda x: (-x[1], x[0])):
    print(score, name)