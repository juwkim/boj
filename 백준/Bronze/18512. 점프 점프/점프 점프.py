X, Y, P1, P2 = map(int, input().split())
flag = 0
for i in range(100):
    a = (P2 - P1 + Y * i) / X
    if a == int(a) and a > -1:
        flag = 1
        break
print(P2 + Y * i if flag else -1)