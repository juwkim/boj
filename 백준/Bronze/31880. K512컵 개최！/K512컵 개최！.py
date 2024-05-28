g = lambda: map(int, input().split())

input()
P = sum(g())
for num in g():
    if num: P *= num
print(P)