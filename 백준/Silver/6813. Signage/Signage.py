def output():
    if len(l) == 1:
        print(l[0] + "." * (W - cnt))
    else:
        q, r = divmod(W - cnt, len(l) - 1)
        for i in range(r):
            print(l[i] + "." * (q + 1), end="")
        for i in range(r, len(l) - 1):
            print(l[i] + "." * q, end="")
        print(l[-1])
W = int(input())
l, cnt = [], 0
for word in ("WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"):
    if cnt + len(l) + len(word) <= W:
        l.append(word)
        cnt += len(word)
    else:
        output()
        l, cnt = [word], len(word)
output()