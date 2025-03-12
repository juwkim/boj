N, M, K = map(int, input().split())
A, idx = [''] * N, 0
clipboard = ''
for _ in range(M):
    c = input()[0]
    match c:
        case 'B': A[idx] = A[idx][:-1]
        case 'C': clipboard = A[idx][-K:]
        case 'N': idx = (idx + 1) % N
        case 'P': A[idx] += clipboard
        case _: A[idx] += c
print(A[idx][-K:] or 'Empty')