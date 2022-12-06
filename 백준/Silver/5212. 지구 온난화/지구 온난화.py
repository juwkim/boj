g = lambda: [*map(int, input().split())]

R, C = g()
margin = ['.' * (C + 2)]
Map = margin + ['.' + input() + '.' for _ in range(R)] + margin

ans = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(1, 1 + R):
    buf = []
    for j in range(1, 1 + C):
        if Map[i][j] == 'X' and [Map[i + s][j + t] for s, t in zip(dx, dy)].count('.') < 3:
            buf.append('X')
        else:
            buf.append('.')
    if ans or 'X' in buf:
        ans.append(buf)

while 'X' not in ans[-1]:
    ans.pop()

s = 0
while all(ans[i][s] == '.' for i in range(len(ans))):
    s += 1

e = C - 1
while all(ans[i][e] == '.' for i in range(len(ans))):
    e -= 1
    
for l in ans:
    print(*l[s:e+1], sep='')