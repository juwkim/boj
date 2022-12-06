N, M = map(int, input().split())
array = [[*map(int, input().split())] + [0, 0, 0] for _ in range(N)]
for _ in range(3):
    array.append([0 for _ in range(M+3)])
r = [[sum(array[j][i:i+2]) for i in range(M+2)] for j in range(N+3)]
c = [[array[j][i] + array[j+1][i] for i in range(M+3)] for j in range(N+2)]

ans = 0
for i in range(N):
    for j in range(M):
        temp = []
        temp.append(r[i][j] + r[i][j+2])
        temp.append(c[i][j] + c[i+2][j])
        temp.append(r[i][j] + r[i+1][j])
        temp.append(c[i][j] + r[i+2][j])
        temp.append(c[i][j] + r[i][j+1])
        temp.append(r[i][j] + c[i+1][j+1])
        temp.append(r[i+1][j] + c[i][j+2])
        temp.append(r[i+2][j] + c[i][j+1])
        temp.append(r[i][j] + c[i][j+2])
        temp.append(r[i][j] + c[i+1][j])
        temp.append(c[i][j] + r[i+1][j+1])
        temp.append(c[i][j] + c[i+1][j+1])
        temp.append(r[i][j+1] + r[i+1][j])
        temp.append(c[i][j+1] + c[i+1][j])
        temp.append(r[i][j] + r[i+1][j+1])
        temp.append(r[i+1][j+1] + array[i][j+1] + array[i+1][j])
        temp.append(c[i][j] + array[i+1][j+1] + array[i+2][j])
        temp.append(r[i][j] + array[i][j+2] + array[i+1][j+1])
        temp.append(c[i][j+1] + array[i+1][j] + array[i+2][j+1])
        ans = max(ans, *temp)
print(ans)