import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import combinations

N, M = g()
solution = g()
models = [g() for _ in range(N)]
best = max(sum(a == b for a, b in zip(solution, model)) for model in models)
ans = 0
for l in range(3, N + 1, 2):
    for choices in combinations(models, l):
        vote = [0] * M
        for i, choice in enumerate(zip(*choices)):
            if choice.count(1) * 2 > l:
                vote[i] = 1
        score = sum(a == b for a, b in zip(solution, vote))
        if score > best:
            ans = 1
            break
    if ans:
        break
print(ans)