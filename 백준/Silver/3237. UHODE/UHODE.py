import sys
input = sys.stdin.readline

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
S = set()
for i in range(-1, 2):
    for j in range(-1, 2):
        S.add((i, j))

input()
x, y = 0, 0
for c in input():
    if c == "I":
        x += 1
        S.add((x + 1, y - 1)); S.add((x + 1, y)); S.add((x + 1, y + 1))
    elif c == "Z":
        x -= 1
        S.add((x - 1, y - 1)); S.add((x - 1, y)); S.add((x - 1, y + 1))
    elif c == "S":
        y += 1
        S.add((x - 1, y + 1)); S.add((x, y + 1)); S.add((x + 1, y + 1))
    else:
        y -= 1
        S.add((x - 1, y - 1)); S.add((x, y - 1)); S.add((x + 1, y - 1))
ans = [i + 1 for i in range(N) if P[i] in S]
if ans:
    for i in ans:
        print(i)
else:
    print(-1)