import sys
input = sys.stdin.readline

n = int(input())
peoples = [[*map(int, input().split())][1:] for _ in range(n)]
l = [0] * 100001
for people in reversed(peoples):
    cur = max(l[p] for p in people) + 1
    for p in people:
        l[p] = max(l[p], cur)
print(max(l))