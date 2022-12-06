from itertools import chain
R, C = map(int, input().split())
check = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
for i in range(R):
    S = input()
    for j in range(C):
        if S[j] == '#':
            for k in range(2):
                check[i+k][j] = -10
                check[i+k][j+1] = -10
        elif S[j] == 'X':
            for k in range(2):
                check[i+k][j] += 1
                check[i+k][j+1] += 1

a = [*chain(*[check[i][1:-1] for i in range(1, R)])]
for k in range(5):
    print(a.count(k))