g = lambda: input().split()

n = int(input())
if n&1:
    print('bad')
else:
    res = set()
    for i in zip(g(), g()):
        if i[0] == i[1]:
            res = set()
            break
        res.update((i, i[::-1]))
    if len(res) == n:
        print('good')
    else:
        print('bad')