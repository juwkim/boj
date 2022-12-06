n = int(input())
teams = [input().split() for _ in range(n)]
solved = [4 - team.count('0') for team in teams]
penalty = [sum([(int(team[i-1])-1)*20 + int(team[i]) for i in range(2, 9, 2) if int(team[i])]) for team in teams]

if solved.count(max(solved)) == 1:
    a = solved.index(max(solved))
else:
    k = max(solved)
    a = penalty.index(min([penalty[i] for i in range(4) if solved[i] == k]))
print(teams[a][0], solved[a], penalty[a])