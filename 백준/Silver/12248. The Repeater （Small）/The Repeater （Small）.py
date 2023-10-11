import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    Set = set()
    buf = [input() for _ in range(int(input()))]
    l = []
    for s in buf:
        prev, tmp, le = '', [], []
        cur = 0
        for c in s:
            if c == prev:
                cur += 1
            else:
                tmp.append(c)
                prev = c
                if cur:
                    le.append(cur)
                cur = 1
        Set.add(''.join(tmp))
        le.append(cur)
        l.append(le)
    if len(Set) != 1:
        print(f"Case #{tc}: Fegla Won")
        continue
    ans = 0
    for p in zip(*l):
        q, r = divmod(sum(p), len(p))
        if r * 2 >= len(p):
            q += 1
        ans += sum(abs(q - x) for x in p)
    print(f"Case #{tc}: {ans}")