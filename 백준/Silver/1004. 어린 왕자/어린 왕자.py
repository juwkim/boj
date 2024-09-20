import math

for _ in range(int(input())):
    points = [*map(int, input().split())]
    ans = 0
    for i in range(int(input())):
        planet = [*map(int, input().split())]
        ans += (math.dist((points[0], points[1]), (planet[0], planet[1])) > planet[2]) ^ (math.dist((points[2], points[3]), (planet[0], planet[1])) > planet[2])
    print(ans)