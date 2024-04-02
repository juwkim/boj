N = int(input())
votes = [list(map(int, input().split())) for _ in range(N)]
votes = [sorted(vote) for vote in zip(*votes)]
winner = max(votes, key=lambda x: (sum(x), x.count(3), x.count(2)))
if votes.count(winner) == 1:
    print(votes.index(winner) + 1, sum(winner))
else:
    print(0, sum(winner))