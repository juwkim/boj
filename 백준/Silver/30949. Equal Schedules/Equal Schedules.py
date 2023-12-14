import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

dic = defaultdict(int)
while True:
    l = input()
    if l[0] == '-':
        break
    s, e, t = l.split()
    dic[t] -= int(e) - int(s)

while True:
    l = input()
    if l[0] == '=':
        break
    s, e, t = l.split()
    dic[t] += int(e) - int(s)

if all(v == 0 for v in dic.values()):
    print("No differences found.")
else:
    for k, v in sorted(dic.items()):
        if v != 0:
            print("%s %+d" % (k, v))