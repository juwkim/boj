l = [['.'] * 6 for _ in range(5)]
for _ in range(int(input())):
    c = input()[0]
    i, j = divmod(ord(c) - 97, 6)
    l[i][j] = c
for i in range(4):
    print(*l[i], sep='')
print(l[4][0] + l[4][1])