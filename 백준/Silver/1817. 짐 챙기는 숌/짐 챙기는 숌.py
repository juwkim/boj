g = lambda: [*map(int, input().split())]

N, M = g()
if N:
    cnt = 0
    capa = M
    books = g()
    for book in books:
        if book == capa:
            cnt += 1
            capa = M
        elif book < capa:
            capa -= book
        else:
            cnt += 1
            capa = M - book
    if capa != M:
        cnt += 1
    print(cnt)
else:
    print(0)