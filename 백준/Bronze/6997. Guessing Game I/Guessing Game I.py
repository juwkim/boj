for _ in range(int(input())):
    a, b = input().split()
    p, q = map(lambda x: [i for i in x], [a, b])
    s = 0
    for m, n in zip(p[:], q[:]):
        if m == n:
            s += 1
            p.remove(m)
            q.remove(n)
    t = sum(min(p.count(i), q.count(i)) for i in set(q))
    print(f'For secret = {a} and guess = {b}, {s} circles and {t} squares will light up.')