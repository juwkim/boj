import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import permutations

def solve(N, friends):
    for arrangement in permutations(range(1, 2 ** N + 1)):
        res = True
        for Ei, Ki, friend in friends:
            for round_number in range(1, Ki + 1):
                opponent_index = arrangement.index(Ei) ^ (1 << (round_number - 1))
                opponent = arrangement[opponent_index]
                if opponent in friend:
                    break
            else:
                continue
            break
        else:
            return "YES"
    return "NO"

for t in range(1, int(input()) + 1):
    N, M = g()
    friends = []
    for _ in range(M):
        Ei, Ki, Bi = g()
        friend = g()
        friends.append((Ei, Ki, set(friend)))
    answer = solve(N, friends)
    print(f"Case #{t}: {answer}")