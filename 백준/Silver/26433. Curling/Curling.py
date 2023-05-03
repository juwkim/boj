g = lambda: [*map(int, input().split())]

from math import dist

for case in range(1, 1 + int(input())):
    rs, rh = g()
    
    stone = []
    for _ in range(int(input())):
        stone.append((dist(g(), (0, 0)) - rs, 0))
    for _ in range(int(input())):
        stone.append((dist(g(), (0, 0)) - rs, 1))
    
    score = [0, 0]
    if stone:
        stone.sort()
        winner = stone[0][1]
        for d, who in stone:
            if d > rh or who != winner:
                break
            score[winner] += 1
    print(f'Case #{case}:', *score)