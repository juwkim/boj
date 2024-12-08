import sys
input = sys.stdin.readline

l = [[], []]
for i in range(1, 1 + int(input())):
    x, y = map(int, input().split())
    l[(x^y)&1].append(i)
if all(l):
    print("YES")
    print(*l[0], *l[1])
else:
    print("NO")