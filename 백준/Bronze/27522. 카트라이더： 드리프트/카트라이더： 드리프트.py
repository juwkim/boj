team = [0, 0]
ranks = sorted(input() for _ in range(8))
for score, line in zip((10, 8, 6, 5, 4, 3, 2, 1), ranks):
    team[line[-1] == 'B'] += score

print(('Red', 'Blue')[team[0] < team[1]])