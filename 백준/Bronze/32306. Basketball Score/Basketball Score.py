a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
score1 = a1 + b1 * 2 + c1 * 3
score2 = a2 + b2 * 2 + c2 * 3
print((0, 1, 2)[(score1 > score2) - (score1 < score2)])