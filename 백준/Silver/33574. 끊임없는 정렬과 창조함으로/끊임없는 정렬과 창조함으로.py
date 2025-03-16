import sys
input = sys.stdin.readline

S = []
for _ in range(int(input())):
    cmd, x, *t = map(int, input().split())
    if cmd == 1:
        if x == 1:
            S.sort()
        else:
            S.sort(reverse=True)
    else:
        t = t[0]
        if x == 0:
            S = [t] + S
        elif x == len(S):
            S.append(t)
        else:
            S = S[:x] + [t] + S[x:]
print(len(S))
print(*S)