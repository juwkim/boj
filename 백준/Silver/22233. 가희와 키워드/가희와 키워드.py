import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
keyword = {input() for _ in range(N)}
for _ in range(M):
    for word in input().split(','):
        keyword.discard(word)
    print(len(keyword))