import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

S = input()
rhyme = []
for _ in range(int(input())):
    l = input().split()
    if any(S.endswith(x) for x in l):
        rhyme.append(l)

for _ in range(int(input())):
    P = input()
    if any(any(P.endswith(x) for x in l) for l in rhyme):
        print("YES")
    else:
        print("NO")