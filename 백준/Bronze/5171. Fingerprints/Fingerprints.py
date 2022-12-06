g = lambda: [*map(int, input().split())]


n, k = g()
finger = [''.join([input() for _ in range(5)]) for _ in range(n)]

for cnt in range(1, 1 + k):
    s = ''.join([input() for _ in range(5)])
    buf = [sum(i != j for i, j in zip(s, fin)) for fin in finger]
    Min = min(buf)
    res = [i + 1 for i in range(n) if buf[i] == Min]
    
    print(f'Data Set {cnt}:')
    print(*res)
    print()