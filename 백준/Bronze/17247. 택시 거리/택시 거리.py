input()
row, a = 0, []
while len(a) != 4:
    col = input().find('1')
    if col != -1:
        a += [row, col]
    row += 1
print(a[2] - a[0] + abs(a[3] - a[1]) // 2)