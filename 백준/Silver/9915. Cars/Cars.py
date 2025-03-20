n, v, d, t = map(int, input().split())
cars = [[0, -i * d] for i in range(n)]
cars[0][0] = v
ans = -1
for _ in range(t):
    for i in range(n):
        cars[i][1] += 5 * cars[i][0]
    if any(cars[i + 1][1] >= cars[i][1] for i in range(n - 1)):
        break
    if n >= 2:
        if cars[0][1] - cars[1][1] < 80:
            cars[0][0] += 5
        elif cars[0][1] - cars[1][1] >= 100:
            cars[0][0] = max(0, cars[0][0] - 5)
    for i in range(n - 1):
        if cars[i][1] - cars[i + 1][1] < 80:
            cars[i + 1][0] = max(0, cars[i + 1][0] - 5)
        elif cars[i][1] - cars[i + 1][1] >= 100:
            cars[i + 1][0] += 5
else:
    ans = cars[0][1]
print(ans)