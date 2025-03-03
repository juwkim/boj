g = lambda: map(int, input().split())

N, M = g()
U, V = g()
texture = [input() for _ in range(U)]
ans = []
match input()[0]:
    case 'c':
        for i in range(min(N, U)):
            ans.append(texture[i][:M] + texture[i][-1] * max(M - V, 0))
        for _ in range(max(N - U, 0)):
            ans.append(ans[-1])
    case 'r':
        for i in range(N):
            l = [texture[i % U][j % V] for j in range(M)]
            ans.append(''.join(l))
    case 'm':
        for i in range(N):
            l = []
            x = i % (2 * U)
            for j in range(M):
                y = j % (2 * V)
                l.append(texture[min(x, 2 * U - 1 - x)][min(y, 2 * V - 1 - y)])
            ans.append(''.join(l))
for l in ans:
    print(l)