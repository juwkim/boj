import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    C = int(input())
    S1, S2, S12 = input(), input(), input()
    check = {(S1, S2)}
    cnt = 0
    while True:
        cnt += 1
        P = "".join(S2[i] + S1[i] for i in range(C))
        if P == S12:
            break
        S1, S2 = P[:C], P[C:]
        if (S1, S2) in check:
            cnt = -1
            break
        check.add((S1, S2))
    print(cnt)