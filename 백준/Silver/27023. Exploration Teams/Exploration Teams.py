import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

C, A = g()
ability_mask = [0] * A
for i in range(A):
    K, *cows = g()
    for cow in cows:
        ability_mask[i] |= 1 << cow - 1
print(sum(all(mask & am for am in ability_mask) for mask in range(1, 1 << C)))