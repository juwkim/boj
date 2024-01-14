import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

spica = [[] for _ in range(13)]
for _ in range(12):
    a, b = g()
    spica[a].append(b)
    spica[b].append(a)

for i in range(1, 13):
    if len(spica[i]) == 3 and sorted(len(spica[j]) for j in spica[i]) == [1, 2, 3]:
        print(i)
        break