import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    buf = []
    for _ in range(4):
        w = input().split()[-1].lower()
        i = len(w) - 1
        while i >= 0 and w[i] not in 'aeiou':
            i -= 1
        if i == -1:
            buf.append(w)
        else:
            buf.append(w[i:])
    s1, s2, s3, s4 = buf
    if s1 == s2 == s3 == s4:
        ans = 'perfect'
    elif s1 == s2 and s3 == s4:
        ans = 'even'
    elif s1 == s3 and s2 == s4:
        ans = 'cross'
    elif s1 == s4 and s2 == s3:
        ans = 'shell'
    else:
        ans = 'free'
    print(ans)