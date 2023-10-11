import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    N = int(input())
    buf = [input() for _ in range(N)]
    Set = set()
    l = []
    for s in buf:
        prev, s_tmp, l_tmp = '', [], []
        cur = 0
        for c in s:
            if c == prev:
                cur += 1
            else:
                s_tmp.append(c)
                prev = c
                if cur:
                    l_tmp.append(cur)
                cur = 1
        Set.add(''.join(s_tmp))
        l_tmp.append(cur)
        l.append(l_tmp)
    if len(Set) != 1:
        print(f"Case #{tc}: Fegla Won")
        continue
    ans = 0
    for p in zip(*l):
        ans += min(sum(abs(q - x) for x in p) for q in range(min(p), max(p) + 1))
    print(f"Case #{tc}: {ans}")