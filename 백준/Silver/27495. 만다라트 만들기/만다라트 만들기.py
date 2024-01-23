import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

mandarat = [input().split() for _ in range(9)]
dic = {}
for i, j in (1, 1), (1, 4), (1, 7), (4, 1), (4, 7), (7, 1), (7, 4), (7, 7):
    l = []
    for p in range(i - 1, i + 2):
        for q in range(j - 1, j + 2):
            if p == i and q == j:
                continue
            l.append(mandarat[p][q])
    l.sort()
    dic[mandarat[i][j]] = l
for i, k in enumerate(sorted(dic), 1):
    print(f"#{i}. {k}")
    for j, v in enumerate(dic[k], 1):
        print(f"#{i}-{j}. {v}")