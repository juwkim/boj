g = lambda: [*map(int, input().split())]

from itertools import combinations
for _ in range(1, 1 + int(input())):
    n = int(input())
    if all(i - j != j - k for i, j, k in combinations(g(), 3)):
        print(f'Case #{_}: YES')
    else:
        print(f'Case #{_}: NO')