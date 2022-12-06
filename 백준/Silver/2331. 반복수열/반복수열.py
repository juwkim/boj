g = lambda: [*map(int, input().split())]
check = set()
A, P = g()
D = [A]
while D[-1] not in check:
    check.add(D[-1])
    D.append(sum(int(i) ** P for i in str(D[-1])))
print(D.index(D[-1]))