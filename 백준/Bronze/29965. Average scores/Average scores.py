import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from statistics import mean

M, J = [], []
for _ in range(int(input())):
    C, P = input().split()
    if C == 'M':
        M.append(int(P))
    else:
        J.append(int(P))
meanM = mean(M) if M else 0
meanJ = mean(J) if J else 0
if meanM > meanJ:
    print('M')
elif meanM < meanJ:
    print('J')
else:
    print('V')