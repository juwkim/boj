N = [*input()]
M = [*input()]

a, b = len(N), len(M)
N = ['0'] * (b - a) + N
M = ['0'] * (a - b) + M

S = [a for a, b in zip(N, M) if a >= b]
T = [b for a, b in zip(N, M) if a <= b]

print(int(''.join(S)) if S else 'YODA')
print(int(''.join(T)) if T else 'YODA')