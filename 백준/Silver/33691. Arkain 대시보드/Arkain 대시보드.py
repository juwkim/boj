import sys
input = lambda: sys.stdin.readline().rstrip()

d = {}
for i in range(int(input())): d[input()] = i
s = {input() for _ in range(int(input()))}
print(*sorted(d.keys(), key=lambda x: (x not in s, -d[x])))