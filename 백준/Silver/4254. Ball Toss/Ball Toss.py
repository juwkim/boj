import sys
input = sys.stdin.readline

while (s := input().rstrip()) != '0':
    n, k, *t = s.split()
    n, k = int(n), int(k) - 1
    visited = bytearray(n + 1)
    m, cnt, tossed = 0, 0, 0
    while tossed < n:
        cnt += 1
        if not visited[k]:
            visited[k] = True
            tossed += 1
        m, cur = k, m
        match t[k]:
            case 'L':
                t[k] = 'R'
                k = (cur - 1) % n
                if k == m:
                    k = (k - 1) % n
            case 'R':
                t[k] = 'L'
                k = (cur + 1) % n
                if k == m:
                    k = (k + 1) % n
    print(f"Classmate {m + 1} got the ball last after {cnt} tosses.")