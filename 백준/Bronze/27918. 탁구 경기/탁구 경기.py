X, Y = 0, 0
for _ in range(int(input())):
    if input() == 'D':
        X += 1
    else:
        Y += 1
    if abs(X - Y) == 2:
        break
print(f'{X}:{Y}')