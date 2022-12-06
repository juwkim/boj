tab = [0] * 366
spa = [0] * 366
max_day = 0
for _ in range(int(input())):
    c, s, e = input().split()
    s, e = map(int, [s, e])
    max_day = max(max_day, e - s + 1)
    if c == 'T':
        for i in range(s-1, e):
            tab[i] += 1
    else:
        for i in range(s-1, e):
            spa[i] += 1
print(sum(i + j != 0 for i, j in zip(tab, spa)))
print(max(i + j for i, j in zip(tab, spa)))
print(sum(i and j and i == j for i, j in zip(tab, spa)))
p = [i + j for i, j in zip(tab, spa) if i == j]
print(max(p) if p else 0)
print(max_day)