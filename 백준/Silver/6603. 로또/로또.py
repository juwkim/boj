from itertools import combinations
while (s := input()) != '0':
    k, *S = s.split()
    for nums in combinations(S, 6):
        print(*nums)
    print()