import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

a, b = input(), input()
v1 = None
for i in range(1, len(a)):
    if a[i] in "aeiou":
        v1 = i
        break
v2 = None
for i in range(len(b) - 2, -1, -1):
    if b[i] in "aeiou":
        v2 = i
        break
if v1 is None and v2 is None:
    ans = a + 'o' + b
elif v2 is None:
    ans = a[:v1 + 1] + b
elif v1 is None:
    ans = a + b[v2:]
else:
    ans = a[:v1] + b[v2:]
print(ans)