from math import dist, sqrt
while (s:= input().rstrip('.')) != "END":
    
    x, y = 0, 0
    for l in s.split(','):
        if l[-2:].isalpha():
            num = int(l[:-2])
            x += [-num, num][l[-1] == 'E'] / sqrt(2)
            y += [-num, num][l[-2] == 'N'] / sqrt(2)
        else:
            num = int(l[:-1])
            if l[-1] == 'E':
                x += num
            elif l[-1] == 'W':
                x -= num
            elif l[-1] == 'N':
                y += num
            else:
                y -= num
    print(f"You can go to ({x:.3f},{y:.3f}), the distance is {dist((0, 0), (x, y)):.3f} steps.")