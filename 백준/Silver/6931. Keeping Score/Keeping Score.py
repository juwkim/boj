import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
import re

score = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}

C, D, H, S = re.split('C|D|H|S', input())[1:]
C_score = sum(score.get(c, 0) for c in C) + max(0, 3 - len(C))
D_score = sum(score.get(d, 0) for d in D) + max(0, 3 - len(D))
H_score = sum(score.get(h, 0) for h in H) + max(0, 3 - len(H))
S_score = sum(score.get(s, 0) for s in S) + max(0, 3 - len(S))
print("Cards Dealt              Points")
print('Clubs', *C, C_score)
print('Diamonds', *D, D_score)
print('Hearts', *H, H_score)
print('Spades', *S, S_score)
print('Total', C_score + D_score + H_score + S_score)