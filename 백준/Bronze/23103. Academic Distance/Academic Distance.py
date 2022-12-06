dist = 0
n = int(input())
new_x, new_y = map(int, input().split())
for _ in range(n - 1):
    x, y = new_x, new_y
    new_x, new_y = map(int, input().split())
    dist += abs(x - new_x) + abs(y - new_y)
print(dist)