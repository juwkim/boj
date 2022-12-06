def trace(start, game, guess):
    for i, change in enumerate(game):
        if start[i] in change:
            start.append(sum(change) - start[i])
        else:
            start.append(start[i])
    return sum([start[i+1] == guess[i] for i in range(N)])
N = int(input())
game = [[*map(int, input().split())] for _ in range(N)]
guess = [i.pop() for i in game]
print(max([*map(lambda x: trace(x, game, guess), [[1], [2], [3]])]))