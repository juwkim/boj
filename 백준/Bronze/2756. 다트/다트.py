from math import ceil
from statistics import median
for _ in range(int(input())):
    dart = [*map(float, input().split())]
    player_1, player_2 = 0, 0
    for i in range(3):
        dist = (dart[2*i]**2 + dart[2*i+1]**2)**.5
        player_1 += 20*median([5, 6 - ceil(dist/3), 0])
    for i in range(3, 6):
        dist = (dart[2*i]**2 + dart[2*i+1]**2)**.5
        player_2 += 20*median([5, 6 - ceil(dist/3), 0])
    if player_1 > player_2:
        state = 'PLAYER 1 WINS.'
    elif player_1 < player_2:
        state = 'PLAYER 2 WINS.'
    else:
        state = 'TIE.'
    print(f'SCORE: {int(player_1)} to {int(player_2)}, {state}')