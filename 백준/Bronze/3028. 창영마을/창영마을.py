now = 1
game = {'A':[1, 2], 'B':[2, 3], 'C':[1, 3]}
for change in input():
    if now in game[change]:
        now = sum(game[change]) - now
print(now)