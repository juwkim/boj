l = enumerate("ABC DEF GHI JKL MNO PQRS TUV WXYZ".split(), 2)
dic = {c: idx for idx, alpha in l for c in alpha}

for _ in range(int(input())):
    ans = []
    for c in input():
        if c.isnumeric():
            ans.append(c)
        elif c.isalpha():
            ans.append(dic[c])
        if len(ans) in (3, 7):
            ans.append('-')
        elif len(ans) == 12:
            break
    print(*ans, sep='')