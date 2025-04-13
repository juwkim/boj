a, b = input().split('.')
ans = []
if int(a) < 5:
    w = 10**len(b)
    num = (10 - int(a)) * w - int(b)
    for i in range(1, 10):
        for l in range(1, 9):
            q, r = divmod(i * (10**l - 1) * w, num)
            if r == 0:
                s = str(q)
                if len(s) == l and int(s[0]) == i:
                    ans.append(q)
if ans:
    print(*sorted(ans), sep="\n")
else:
    print("No solution")