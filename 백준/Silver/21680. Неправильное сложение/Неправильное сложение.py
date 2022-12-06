def Sum(x, y):
    if len(x) < len(y):
        x = '0' * (len(y) - len(x)) + x
    else:
        y = '0' * (len(x) - len(y)) + y
    
    res = []
    for a, b in zip(x, y):
        res.append(str(int(a) + int(b)))
    
    return ''.join(res)

a, b, c = input().split()
buf = set([Sum(Sum(a, b), c), Sum(Sum(b, c), a), Sum(Sum(c, a), b)])
print(['YES', 'NO'][len(buf) == 1])
for num in sorted(buf, key=int):
    print(num)