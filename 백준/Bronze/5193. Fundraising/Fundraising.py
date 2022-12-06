g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    c, d, t = g()
    buf = [[0] * c for _ in range(d)]
    for _ in range(t):
        di, ci, mi = g()
        buf[di-1][ci-1] += mi
    
    violators = []
    for i in range(d):
        Sum = 0
        for num in buf[i]:
            Sum += num
            if num > 2100 or Sum > 40000:
                violators.append(i+1)
                break
    print(f'Data Set {cnt}:')
    if violators:
        print('Violators:')
        for Violator in violators:
            print(Violator)
    else:
        print('No violations')