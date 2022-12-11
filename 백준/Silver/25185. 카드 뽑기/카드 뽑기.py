from itertools import combinations
for _ in range(int(input())):
    ans = ':('
    A, B, C, D = sorted(input().split())
    if A == B and C == D:
        ans = ':)'
    elif A == B == C or B == C == D:
        ans = ':)'
    elif any(int(i[0]) + 2 == int(j[0]) + 1 == int(k[0]) and i[1] == j[1] == k[1] for i, j, k in combinations([A, B, C, D], 3)):
        ans = ':)'
    print(ans)