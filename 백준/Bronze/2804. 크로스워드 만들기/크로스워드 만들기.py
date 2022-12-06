from itertools import product
A, B = input().split()
N, M = map(len, [A, B])
for i,j in product(range(N), range(M)):
    if A[i] == B[j]:
        break
for k in range(M):
    if k == j:
        print(A)
    else:
        print('.' * i + B[k] + '.' * (N - i - 1))