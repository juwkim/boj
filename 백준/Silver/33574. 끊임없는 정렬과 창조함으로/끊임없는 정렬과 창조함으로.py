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
        S.insert(x, t[0])
print(len(S))
print(*S)