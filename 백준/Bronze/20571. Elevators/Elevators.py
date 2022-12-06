from math import ceil
S, N = input().split()
N = int(N)
print(0 if N == 1 else ceil(N/5) if S[0] == 'r' else ceil(N/7) if S[0] == 'c' else ceil(N/4))