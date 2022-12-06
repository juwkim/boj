def change(alpha):
    s = '.O-|/\\^<v>'.index(alpha)
    return '.O|-\\/<v>^'[s]

N, M = map(int, input().split())
milk = [*zip(*[input() for _ in range(N)])][::-1]

for i in range(M):
    for alpha in milk[i]:
        print(change(alpha), end='')
    print()