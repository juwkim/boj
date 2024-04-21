from collections import Counter

def solve(l):
    cnt = Counter()
    for v in l.split('+'):
        cur = Counter()
        i, mul = 0, 1
        if v[0].isdigit():
            mul = int(v[0])
            i += 1
        while i < len(v):
            if i + 1 < len(v) and v[i + 1].isdigit():
                cur[v[i]] += int(v[i + 1])
                i += 2
            else:
                cur[v[i]] += 1
                i += 1
        for k, v in cur.items():
            cnt[k] += v * mul
    return cnt

for _ in range(int(input())):
    a, b = input().split("->")
    if solve(a) == solve(b):
        print("DA")
    else:
        print("NE")