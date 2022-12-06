from math import sin, cos, pi
for _ in [0]*int(input()):
    x, y, angle = 0, 0, 0 
    for _ in [0]*int(input()):
        co, n = input().split()
        if co in 'fdbk':
            x += cos(angle) * int(n) * (-1)**(co == 'bk')
            y += sin(angle) * int(n) * (-1)**(co == 'bk')
        else:
            angle += int(n) *pi/180 * (-1)**(co == 'rt')
    print(round((x**2 + y**2)**.5))