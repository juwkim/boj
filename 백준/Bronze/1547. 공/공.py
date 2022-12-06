M = int(input())
pos = 1
for _ in range(M):
    X, Y = map(int, input().split())
    if pos == X:
        pos = Y
    elif pos == Y:
        pos = X
print(pos)