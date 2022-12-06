T = int(input())

for i in range(1, T+1):
    points = list(map(int, input().split()))
    print("Case #{0}: {1} + {2} = {3}".format(i, points[0], points[1], points[0] + points[1]))