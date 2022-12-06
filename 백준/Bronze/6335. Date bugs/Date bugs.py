g = lambda: [*map(int, input().split())]

cnt = 1
while n:= int(input()):
    years = [g() for _ in range(n)]
    
    a, b, c = zip(*years)
    year = max(b)
    msg = f'Case #{cnt}:\nUnknown bugs detected.\n'
    while year < 10000:
        if all(i == (year - j) % (k - j) + j for i, j, k in zip(a, b, c)):
            msg = f'Case #{cnt}:\nThe actual year is {year}.\n'
            break
        year += 1
    print(msg)
    cnt += 1