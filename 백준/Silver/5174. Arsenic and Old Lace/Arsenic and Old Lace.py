import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations

for tc in range(1, int(input()) + 1):
    s, b = map(int, input().split())
    masks = []
    for _ in range(b):
        mask = 0
        for i, c in enumerate(input()):
            if c == 'y':
                mask |= 1 << i
        masks.append(mask)
    target = 0
    for i, c in enumerate(input()):
        if c == 'y':
            target |= 1 << i
    ans = "Impossible."
    for k in range(1, b + 1):
        for comb in combinations(range(b), k):
            combined = 0
            for idx in comb:
                combined |= masks[idx]
            if combined == target:
                ans = k
                break
        else:
            continue
        break
    print(f"Data Set {tc}:\n{ans}\n")