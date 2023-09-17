import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, D = g()
D -= 1
dic = {'d': "qb", 'b': "pd", 'q': "dp", 'p': "bq"}
for _ in range(N):
    print(*[dic[c][D] for c in input()], sep='')