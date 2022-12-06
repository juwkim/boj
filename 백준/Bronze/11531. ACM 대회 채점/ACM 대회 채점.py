log = []
while (s:=input()) != '-1':
    log.append(s.split()) 
right = [*filter(lambda x: x[2] == 'right', log)]
if right:
    s, t = map(lambda x: [*zip(*x)], [log, right])
    print(len(right), sum(map(int, t[0])) + 20 * (sum(s[1].count(i) for i in t[1]) - len(right)))
else:
    print(0, 0)