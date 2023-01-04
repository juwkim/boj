N, M, K = map(int, input().split())
S = input()
mat = [[*input()] for _ in range(N)]
for move in S:
    if move in 'L':
        for i in range(N):
            idx = 0
            for j in range(M):
                if mat[i][j] != '.':
                    mat[i][idx] = mat[i][j]
                    idx += 1
            while idx < M:
                mat[i][idx] = '.'
                idx += 1
    elif move == 'R':
        for i in range(N):
            idx = M - 1
            for j in range(M-1, -1, -1):
                if mat[i][j] != '.':
                    mat[i][idx] = mat[i][j]
                    idx -= 1
            while idx >= 0:
                mat[i][idx] = '.'
                idx -= 1
    elif move == 'U':
        for j in range(M):
            idx = 0
            for i in range(N):
                if mat[i][j] != '.':
                    mat[idx][j] = mat[i][j]
                    idx += 1
            while idx < N:
                mat[idx][j] = '.'
                idx += 1
    else:
        for j in range(M):
            idx = N - 1
            for i in range(N - 1, -1, -1):
                if mat[i][j] != '.':
                    mat[idx][j] = mat[i][j]
                    idx -= 1
            while idx >= 0:
                mat[idx][j] = '.'
                idx -= 1
for line in mat:
    print(*line, sep='')