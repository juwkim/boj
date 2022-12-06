order = 1
while(True):
    n = int(input())
    if n < 0:
        break
    points = [[*map(int, input().split())] for _ in range(n)]
    mass = sum(i[2] for i in points)
    x = sum(i[0]*i[2] for i in points) / mass
    y = sum(i[1]*i[2] for i in points) / mass
    print(f'Case {order}: {x:.2f} {y:.2f}')
    order += 1
    input()