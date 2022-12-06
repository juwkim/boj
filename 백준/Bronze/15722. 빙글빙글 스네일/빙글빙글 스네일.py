n, i = int(input()), 1
x, y, direction = 0, 0, 0
check_1, check_2 = 0, 0
while n:
    if check_1 == i:
        direction = (direction + 1) % 4
        i += check_2
        check_2 = 1 - check_2
        check_1 = 0
    
    if direction == 0:
        y += 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y -= 1
    else:
        x -= 1
    check_1 += 1
    n -= 1

print(x, y)