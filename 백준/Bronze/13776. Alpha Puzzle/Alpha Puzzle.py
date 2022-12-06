N = int(input())
ans = ''
res = set(' ')
while len(res) != 27:
    for c in input():
        if not c in res:
            res.add(c)
            ans += c
print(ans)