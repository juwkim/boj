for _ in range(int(input())):
    a, b, k = input().split(' ')
    h1, m1, s1 = map(int, a.split(':'))
    h2, m2, s2 = map(int, b.split(':'))
    k = int(k) * 60
    t1 = (h1 * 60 + m1) * 60 + s1
    t2 = (h2 * 60 + m2) * 60 + s2
    c = (t2 - t1 - 1) % 86400 + 1
    if k <= c:
        print('Perfect')
    elif k <= c + 3600:
        print('Test')
    else:
        print('Fail')