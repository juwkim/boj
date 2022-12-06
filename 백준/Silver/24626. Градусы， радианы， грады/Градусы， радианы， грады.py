from math import pi

EPS = 1e-6
for _ in range(int(input())):
    q = float(input())
    answer = []
    for a in range(0, 360):
        if abs(a - q) <= EPS:
            answer.append((a, 1))
        if abs(a * pi / 180 - q) <= EPS:
            answer.append((a, 2))
        if abs(a * 10 / 9 - q) <= EPS:
            answer.append((a, 3))

    if len(answer) == 1:
        print(*answer[0])
    else:
        print(-1)