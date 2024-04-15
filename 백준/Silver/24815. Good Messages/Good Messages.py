from collections import Counter

O = int(input())
l = len(msg:=input())
S = Counter(ord(c) - ord('a') for c in msg)
N = int(input())
bad = 0
for _ in range(N):
    S = Counter({(k + O) % 26: v for k, v in S.items()})
    vowel = sum(S[c] for c in (0, 4, 8, 14, 20, 24))
    bad += 3 * vowel >= l
print(("Colleague", "Boris")[N > 2 * bad])