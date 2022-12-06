N = int(input())
pulley = [i[2] for i in sorted([list(map(int, input().split())) for _ in range(N-1)])]
rotation = 0
for change in pulley:
    rotation = (rotation + change) % 2
print(rotation)