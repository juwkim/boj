from collections import deque

O = int(input())
l = len(msg:=input())
dq = deque([0] * 26)
for c in msg: dq[ord(c) - ord('a')] += 1
N = int(input())
bad = 0
for _ in range(N):
    dq.rotate(O)
    vowel = sum(dq[c] for c in (0, 4, 8, 14, 20, 24))
    bad += 3 * vowel >= l
print(("Colleague", "Boris")[N > 2 * bad])