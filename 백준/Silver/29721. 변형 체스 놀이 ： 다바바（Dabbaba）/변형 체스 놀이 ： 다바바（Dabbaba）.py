import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
dababa = set(tuple(map(int, input().split())) for _ in range(K))
pos = set()
for X, Y in dababa:
    for a, b in ((X - 2, Y), (X + 2, Y), (X, Y - 2), (X, Y + 2)):
        if a < 1 or b < 1 or a > N or b > N:
            continue
        if (a, b) in dababa or (a, b) in pos:
            continue
        pos.add((a, b))
print(len(pos))