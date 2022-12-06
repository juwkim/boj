import sys
I = sys.stdin.readline
g = lambda s, x: any(s in i for i in x)
m, n = 'AAA', 'BBB'
for _ in range(int(I())):
    a = [I() for _ in range(5)]
    b = [''.join(i) for i in zip(*a)]
    c = [[''.join(j) for j in zip(a[i], a[i+1][1:], a[i+2][2:])] for i in range(3)]
    d = [[''.join(j) for j in zip(a[i][2:], a[i+1][1:], a[i+2])] for i in range(3)]
    A = g(m, a+b) or g(m, c) or g(m, d)
    B = g(n, a+b) or g(n, c) or g(n, d)
    print('draw' if A and B else 'A wins' if A else 'B wins' if B else 'draw')