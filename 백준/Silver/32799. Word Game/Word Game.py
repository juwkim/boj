from itertools import permutations

def solve(s, idx):
    global best_word, min_length
    if idx == n:
        if len(s) < min_length or (len(s) == min_length and s < best_word):
            min_length = len(s)
            best_word = s
        return
    t = perm[idx]
    for k in range(1, min(len(s), len(t)) + 1):
        if s[-k:] == t[:k]:
            solve(s + t[k:], idx + 1)
        if t[-k:] == s[:k]:
            solve(t + s[k:], idx + 1)

n = int(input())
words = [input() for _ in range(n)]
best_word, min_length = None, float('inf')
for perm in permutations(words):
    solve(perm[0], 1)
print(best_word if best_word else -1)