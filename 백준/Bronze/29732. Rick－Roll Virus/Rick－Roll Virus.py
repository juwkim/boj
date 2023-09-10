import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, K = g()
S = [*input()]

i = 0
while i < N:
    if S[i] == '.':
        i += 1
        continue
    for j in range(i - 1, max(-1, i - 1 - K), -1):
        if S[j] == 'R':
            break
        S[j] = 'R'
    Next = min(N, i + 1 + K)
    for j in range(i + 1, Next):
        if S[j] == 'R':
            Next = j
            break
        S[j] = 'R'
    i = Next
if S.count('R') <= M:
    print("Yes")
else:
    print("No")