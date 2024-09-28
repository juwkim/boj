from itertools import combinations

s = input()
print(sum(all(int(x) < 256 and str(int(x)) == x for x in (s[:i], s[i:j], s[j:k], s[k:])) for i, j, k in combinations(range(1, len(s)), 3)))