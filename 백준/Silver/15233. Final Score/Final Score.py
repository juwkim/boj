g = lambda: [*map(int, input().split())]

A, B, G = g()
player_A = set(input().split())
player_B = set(input().split())
score = 0
for name in input().split():
    score += (name in player_A) - (name in player_B)
if score:
    print('BA'[score>0])
else:
    print('TIE')