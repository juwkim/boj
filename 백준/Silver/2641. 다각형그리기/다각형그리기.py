import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [*map(int, input().split())]
s = set()
for i in range(n):
    l = a[i:] + a[:i]
    s.add(" ".join(map(str, l)))
    s.add(" ".join(map(str, [(0, 3, 4, 1, 2)[num] for num in l[::-1]])))
ans = []
for _ in range(int(input())):
    p = input()
    if p in s:
        ans.append(p)
print(len(ans))
for l in ans:
    print(l)