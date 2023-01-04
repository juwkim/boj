from math import inf
from itertools import combinations
def solution(line):

    points = set()
    x_min, y_min = inf, inf
    x_max, y_max = -inf, -inf
    for (A, B, E), (C, D, F) in combinations(line, 2):

        divisor = A * D - B * C
        if divisor == 0:  # 두 직선이 평행 한 경우
            continue

        x, rx = divmod(B * F - E * D, divisor)
        y, ry = divmod(E * C - A * F, divisor)

        if rx or ry:  # 격자점이 아닌 경우
            continue

        points.add((x, y))

        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x)
        y_max = max(y_max, y)

    answer = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for x, y in points:
        answer[y_max - y][x - x_min] = '*'
    
    answer = [*map(''.join, answer)]
    return answer