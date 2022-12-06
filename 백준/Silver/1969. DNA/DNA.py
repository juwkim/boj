g = lambda: [*map(int, input().split())]

N, M = g()
ans = ''
DNA = [input() for _ in range(N)]
for j in range(M):
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(N):
        dic[DNA[i][j]] += 1
    s = ''
    cnt = 0
    for key in dic:
        if dic[key] > cnt:
            cnt = dic[key]
            s = key
    ans += s

print(ans)
print(sum(sum(x != y for x, y in zip(DNA[i], ans)) for i in range(N)))