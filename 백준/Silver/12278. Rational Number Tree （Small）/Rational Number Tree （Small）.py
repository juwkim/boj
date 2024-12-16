import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    id, *args = map(int, input().split())
    if id == 1:
        n = args[0]
        p, q = 1, 1
        for c in bin(n)[3:]:
            if c == '1':
                p += q
            else:
                q += p
        print(f"Case #{tc}: {p} {q}")
    else:
        p, q = args
        n, num = 0, 1
        while p:
            if p >= q:
                p -= q
                n += num
            else:
                q -= p
            num <<= 1
        print(f"Case #{tc}: {n}")