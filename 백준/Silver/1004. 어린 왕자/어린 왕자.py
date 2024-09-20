import math

for _ in range(int(input())):
    points = [*map(int, input().split())]
    total = 0
    for i in range(int(input())):
        check = 0
        planet = [*map(int, input().split())]
        if math.dist((points[0], points[1]), (planet[0], planet[1])) > planet[2]:
            check += 1
        if math.dist((points[2], points[3]), (planet[0], planet[1])) > planet[2]:
            check += 1
        if check == 1:
            total += 1
    print(total)