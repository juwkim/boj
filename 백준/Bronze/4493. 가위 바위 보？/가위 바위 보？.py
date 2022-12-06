t = int(input())
RSP = {'R':'SRP', 'S':'PSR', 'P':'RPS'}
for _ in range(t):
    n = int(input())
    total = 0
    for _ in range(n):
        player_1, player_2 = input().split()
        total += RSP[player_1].index(player_2) - 1
    print('Player 2' if total > 0 else 'Player 1' if total < 0 else 'TIE')