import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
files = [input() for _ in range(N)]
ext = set(input() for _ in range(M))
for i in range(N):
    idx = files[i].rfind('.')
    if idx != -1 and files[i][idx + 1:] in ext:
        files[i] = [files[i][:idx], files[i][idx + 1:], ""]
    else:
        files[i] = [files[i], '{']
files.sort(key=lambda x: (x[0], -len(x), x[1]))
for file in files:
    if len(file) == 2:
        print(file[0])
    else:
        print(".".join(file[:2]))