a = []
for _ in range(int(input())):
    name, *l = input().split()
    score, risk, cost = map(int, l)
    a.append((-(score**3//(cost * (risk + 1))), cost, name))
a.sort()
print(a[1][2])