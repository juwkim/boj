from itertools import combinations
L, C = map(int, input().split())
for l in combinations(sorted(input().split()), L):
    vowel = sum(c in 'aeiou' for c in l)
    if 1 <= vowel <= L - 2:
        print(*l, sep='')