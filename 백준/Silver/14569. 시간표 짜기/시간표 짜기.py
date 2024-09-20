import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

subject = [set(g()[1:]) for _ in range(int(input()))]
for _ in range(int(input())):
    p, *q = g()
    q = set(q)
    print(sum(s.issubset(q) for s in subject))