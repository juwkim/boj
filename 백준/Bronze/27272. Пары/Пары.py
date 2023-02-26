from itertools import permutations

ans = -1e9
for a, b, c, d in permutations(map(int, input().split()), 4):
    ans = max(ans, a * b + c * d)
print(ans)