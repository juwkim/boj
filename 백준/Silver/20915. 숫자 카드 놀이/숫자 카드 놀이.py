import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    l = [[], []]
    s = sorted(input().replace('6', '9'), reverse=True)
    f = False
    for i in range(0, len(s) - 1, 2):
        a, b = sorted((s[i], s[i + 1]))
        if s[i] == s[i + 1] or f:
            l[0].append(a)
            l[1].append(b)
        else:
            l[0].append(b)
            l[1].append(a)
            f = True
    if len(s) & 1:
        l[1].append(s[-1])
    a, b = int(''.join(l[0])), int(''.join(l[1]))
    print(a * b)