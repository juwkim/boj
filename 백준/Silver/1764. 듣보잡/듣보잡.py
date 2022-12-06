import sys
input = sys.stdin.readline
names = {}
N, M = map(int, input().split())
for _ in range(N):
    names[input().rstrip()] = 1

count = 0
common = []
for _ in range(M):
    try:
        name = input().rstrip()
        count += names[name]
        common += [name]
    except:
        pass
print(count)
print(*sorted(common), sep='\n')