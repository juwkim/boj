from math import comb
while (s := input())[0] != '-':
    G, T, A, D = map(int, s.split())
    
    games = G * comb(T, 2)
    teams = G * A + D
    
    if teams & (teams - 1):
        next_teams = pow(2, len(bin(teams)) - 2)
        add_teams = next_teams - teams
        teams = next_teams
    else:
        add_teams = 0

    games += teams - 1
    print(f'{G}*{A}/{T}+{D}={games}+{add_teams}')