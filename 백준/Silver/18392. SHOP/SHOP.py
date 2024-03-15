import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    M = int(input())
    buf = [[*map(int, l.split(':'))] for l in input().split(',')]
    print(f"Customer{tc}:")
    ans = []
    for m, a in sorted(buf, reverse=True):
        cnt = min(M // m, a)
        if cnt:
            ans.append((m, cnt))
            M -= m * cnt
            if M == 0:
                break
    if M:
        print("Impossible")
    else:
        for m, a in ans:
            print(m, a)