l = [*map(int, input().split())]

a = l.count(0)
if a == 0:
    print(l[0], l[1])
elif a == 1:
    print(l.index(0) + 1, 10 - sum(l))
elif a == 2:
    print(*sorted(set(range(1, 5)) - set(l)))