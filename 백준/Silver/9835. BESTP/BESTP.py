d = {'o': 100, 'e': 10, 'g': 1, 'a': 0, 'b': -1, 'i': -10, 'u': -100}
for s in open(0).read().replace(" ", "").replace("\n", "").rstrip(".").split(','):
    cur = []
    ans, score = 0, 0
    for c in s:
        score += d[c]
        if score < 0:
            cur, score = [], 0
        else:
            cur.append(c)
        ans = max(ans, score)
    print(ans)