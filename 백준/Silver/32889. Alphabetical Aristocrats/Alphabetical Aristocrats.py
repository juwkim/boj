import sys
input = lambda: sys.stdin.readline().rstrip()

l = []
for _ in range(int(input())):
    s, i = input(), 0
    while not s[i].isupper():
        i += 1
    l.append((s[i:], s))
for k, v in sorted(l):
    print(v)