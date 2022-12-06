s, v1, v2 = map(int, input().split())
flag = 0
for i in range(s//v1, -1, -1):
    if ((s - v1 * i) / v2)%1 == 0:
        flag = 1
        break
print(f'{i} {int((s - v1 * i) / v2)}' if flag else 'Impossible')