score = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    d = (x**2 + y**2)**.5
    score += max(0, int(10.5 - d/20))
print(score)