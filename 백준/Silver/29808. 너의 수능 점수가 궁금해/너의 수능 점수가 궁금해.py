import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

q, r = divmod(int(input()), 4763)
if r:
    print(0)
else:
    ans = []
    for a in range(201):
        if a:
            b, r1 = divmod(q - 508 * a, 305)
            if r1 == 0 and 0 <= b <= 200:
                ans.append((a, b))
            b, r1 = divmod(q - 508 * a, 212)
            if r1 == 0 and 1 <= b <= 200:
                ans.append((a, b))
        b, r1 = divmod(q - 108 * a, 305)
        if r1 == 0 and 0 <= b <= 200:
            ans.append((a, b))
        b, r1 = divmod(q - 108 * a, 212)
        if r1 == 0 and 1 <= b <= 200:
            ans.append((a, b))
    print(len(ans))
    for (a, b) in ans:
        print(a, b)