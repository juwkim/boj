g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    
    C, B, n, r = g()
    companies = set(g())
    r /= 100
    cnt = 0
    for i in range(n):
        c, p = g()
        if c in companies:
            cnt += int(p * r)
    print(f'Data Set {_}:\n{cnt}\n')