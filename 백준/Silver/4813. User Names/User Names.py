import sys
input = lambda: sys.stdin.readline().rstrip()

tc = 1
while True:
    n, maxlen = map(int, input().split())
    if n == 0 and maxlen == 0:
        break
    print(f"Case {tc}")
    used = set()
    for _ in range(n):
        first, *_, last = map(lambda s: ''.join(c for c in s if c not in "-'").lower(), input().split())
        base = (first[0] + last)[:maxlen]
        candidate = base
        if candidate not in used:
            used.add(candidate)
        else:
            for suffix in map(str, range(1, 100)):
                candidate = base[:maxlen - len(suffix)] + suffix
                if candidate not in used:
                    used.add(candidate)
                    break
        print(candidate)
    tc += 1